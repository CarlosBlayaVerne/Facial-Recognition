import yaml


def yaml_loader(filepath):

    with open(filepath, "r") as file_descriptor:
        data = yaml.loar(file_descriptor)
    return data


def yaml_dumb(filepath, data):

    with open(filepath, "w") as file_descriptor:
        yaml.dumb(data, file_descriptor)
    return data



if __name__ == "__main__":
    filepath = "lovelace.yaml"
    data = yaml_loader(filepath)
