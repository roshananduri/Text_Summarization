import os
from box.exceptions import BoxValueError
import yaml
from text_summarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

"""
reasons to import ConfigBox:

d={'key':'value','key1':'value1','key2':'value2'}
print(d['key'])
output >> value
but if we want to use d.key it throws error

d=ConfigBox({'key':'value','key1':'value1','key2':'value2'})
print(d.key)
output >> 'value'

"""


'''

reasons to use ensure_annotation decorator:
function input arguments are need to be of one datatype, sometime the function may work fine with
other datatypes but it is not the scope of the project, so to terminate these kinds of mistakes in outputs,
we'll use this decorator.
This will throw an EnsureError if anyother datatype is used.

'''



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''reads yaml file and returns
     Args:
        path_to_yaml: path to yaml file
     Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns: 
        ConfigBox: ConfigBox Type
    '''

    try:
        with open(path_to_yaml )as yaml_file:
               content=yaml.safe_load(yaml_file)
               logger.info(f"yaml file: {path_to_yaml} loaded successfully")
               return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
       raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=False):
    """Create list of directories
    Args:
        path_to_directories: list of directories
        ignore_log (bool, optional): ignore if multiple directories creatred. Defaults to False"""

    for path in path_to_directories:
        os.mkdir(path)
        if verbose:
            logger.info(f"created directory at :{path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path of the file 
    
    Returns:
        str: size in KB
    """    
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} in KB"

 
               
     