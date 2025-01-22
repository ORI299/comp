from flask import Flask, render_template, jsonify, request
import subprocess
import json
import platform
import psutil
from datetime import datetime

app = Flask(__name_