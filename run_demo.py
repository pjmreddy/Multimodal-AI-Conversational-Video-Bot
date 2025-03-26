import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the demo function
from gradio_utils import get_demo

# Create and launch the demo
demo = get_demo()
demo.launch()