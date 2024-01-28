from flask import render_template, Blueprint, abort, send_file
from jinja2 import TemplateNotFound

# TODO: How to ensure consistency of formatting? Is there something like prettier?

swagger_ui_blueprint = Blueprint(
    'swagger_ui',
      __name__,
        static_folder='../../../swagger-ui',
        template_folder='../../../swagger-ui',
          url_prefix='')


@swagger_ui_blueprint.route('/swagger-ui')
def render_swagger_ui():
    try:
        return render_template('/index.html', base_path='/swagger-ui')
    except TemplateNotFound:
        abort(404)


@swagger_ui_blueprint.route('/swagger-definition')
def get_swagger_definition():
    return send_file('open-api.yaml')
