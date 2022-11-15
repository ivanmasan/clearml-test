import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(config):
    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    main()
