"""
Ce fichier contient les fonctions servant à analyser l'entrainement
"""


# Imports de modules tiers
import matplotlib.pyplot as plt


def read_logs(log_path) -> [str]:
    """
    Cette fonction parse le fichier log

    :param str log_path: Chemin du fichier log
    """
    with open(log_path) as logfile:
        lines = logfile.readlines()
    logs = []

    for line in lines[5:]:
        line: str
        if line.startswith('\t'):  # On est à l'intérieur d'une epoch ou d'une itération
            line = line.strip()
            log = logs[-1]
            if line in ("train", "test", "push"):
                log["results"].append({})
            elif len(line.split(":")) == 2:
                key, value = line.split(":")
                value = value.strip().replace('%', '')
                log["results"][-1][key] = float(value)
        else:  # On est à une ligne epoch ou itération
            name, num = line.split(':')
            num = int(num.strip())
            previous_epoch = logs[-1]["previous_epoch"] if name == "iteration" else num
            logs.append({"name": name, "num": num, "previous_epoch": previous_epoch, "results": []})
    return logs


def extract_mesures(logs, stop=None, only_epoch=False):
    mesure_list = ("cross ent", "accu", "cluster", "separation")
    mesures = {}
    for dataset in ("train", "test"):
        for mesure in mesure_list:
            mesures[f"{dataset}_{mesure}"] = []
    for log in logs[:-1]:
        if log["name"] == "epoch" or not only_epoch:
            if stop is not None and stop <= log["num"]:
                break
            for dataset_id, dataset in enumerate(("train", "test")):
                for mesure in mesure_list:
                    mesures[f"{dataset}_{mesure}"].append(log["results"][dataset_id][mesure])
    return mesures


if __name__ == '__main__':
    #logfile_path = "output/train.log"
    logfile_path = "output/train_resnet.log"
    logs = read_logs(logfile_path)
    mesures = extract_mesures(logs)

    plt.plot(mesures["train_cross ent"], label="train")
    plt.plot(mesures["test_cross ent"], label="test")
    plt.legend()
    plt.title("Cross-entopy loss by epoch")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.show()

    plt.plot(mesures["train_accu"], label="train")
    plt.plot(mesures["test_accu"], label="test")
    plt.legend()
    plt.title("Accuracy by epoch")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.show()

    plt.plot(mesures["train_cluster"], label="Cluster")
    plt.plot(mesures["train_separation"], label="Separation")
    plt.legend()
    plt.title("Cluster and separation cost by epoch")
    plt.xlabel("Epoch")
    plt.ylabel("Cost")
    plt.show()



