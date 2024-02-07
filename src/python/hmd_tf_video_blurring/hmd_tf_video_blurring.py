import logging
import subprocess
import sys
import os
import json
from pathlib import Path
import shutil
from typing import Dict

logging.basicConfig(
    stream=sys.stdout,
    format="%(levelname)s %(asctime)s - %(message)s",
    level=logging.ERROR,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def do_transform(
    input_content_path: str,
    output_content_path: str,
    transform_nid: str,
    transform_instance_context: Dict,
) -> int:
    """Function to do the actual Transform work

    Args:
        input_content_path (str): filepath for input files
        output_content_path (str): filepath for output files
        transform_nid (str): NID of running TransformInstance
        transform_instance_context (Dict): context dictionary for the running TransformInstance

    Returns:
        int: exit code
    """
    logger.info(f"Transform_nid: {transform_nid}")
    logger.info(f"Transform_instance_context: {transform_instance_context}")

    videos = os.listdir(input_content_path / "videos")

    for video in videos:
        logger.info(f"Processing: {video}")
        retcode = subprocess.run(
            [
                "deface",
                "--output",
                f"{str(output_content_path / 'out_videos')}/{os.path.splitext(video)[0]}_anonymized{os.path.splitext(video)[-1]}",
                str(input_content_path / "videos" / video),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if retcode.returncode != 0:
            raise Exception(f"Error processing {video}. {retcode.stderr}")

    return 0
