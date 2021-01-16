import os
import warnings

import yaml

warnings.filterwarnings("ignore")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
config_path = os.getenv("TOOL_BOX_CONFIG") or os.path.join(PROJECT_ROOT, "src", "edwards_tool_box",
                                                           "resources/config/conf.yaml")
GLOBAL_CONFIG = yaml.load(open(config_path))
