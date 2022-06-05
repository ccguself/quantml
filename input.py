import os
import numpy as np
import pandas as pd
from .config import configs_input

""" 基础数据结构

    1. 每个文件单元，包含一只标的，过往时间的全部行情数据（暂定为小时K线）

"""


class Input:
    def __init__(self, config=configs_input) -> None:
        self.config = config

    def fetch_data(self):

        pass

