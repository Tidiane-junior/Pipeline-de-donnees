import logging
from pathlib import Path


def setup_logger(
    name: str = "data_pipeline",
    log_file: str = "logs/pipeline.log",
    level: int = logging.INFO
) -> logging.Logger:
    """
    Configure un logger structuré pour le pipeline.
    Args:
        name (str): Le nom du logger.
        log_file (str): Le chemin du fichier de log.
        level (int): Le niveau de log.
    """
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Évite les doublons si relancé
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
