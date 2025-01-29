import logging.config
import os.path

import yaml

base_dir = __file__[: -len("/packages/langfarm-tests/src/langfarm_tests/base_for_test.py")]


def config_log(log_file: str):
    # 读取 yaml 格式的日志配置
    with open(log_file) as f:
        log_config = yaml.full_load(f)
        out_log_file = log_config["handlers"]["file_handler"]["filename"]
        log_dir = f"{base_dir}/logs"
        if not os.path.exists(log_dir):
            print("创建日志目录：", log_dir)
            os.makedirs(log_dir, exist_ok=True)
        log_config["handlers"]["file_handler"]["filename"] = f"{base_dir}/{out_log_file}"
        logging.config.dictConfig(log_config)


logger = logging.getLogger(__name__)


def config_log_for_test():
    # 打印空行
    print()

    log_file = f"{base_dir}/tests/logging.yaml"
    print("配置 log_file = ", log_file)

    config_log(log_file)

    logger.info("配置 log_file = %s", log_file)


config_log_for_test()


def get_test_logger(name: str):
    return logging.getLogger(name)
