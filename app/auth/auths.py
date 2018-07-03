
from flask import Blueprint

auths_bp = Blueprint('auths', __name__, url_prefix="/auths/")


@auths_bp.route('login', methods=['POST'])
def login():
    return 'login'


@auths_bp.route('register', methods=['POST'])
def register():
    return 'register'


@auths_bp.route('logout', methods=['POST'])
def logout():
    return 'logout'
