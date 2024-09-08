from flask import Flask, render_template_string
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

html_template = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Wold Virtual</title>

    <style>

        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; }
        .header { background-color: #4CAF50; color: white; padding: 15px 0; text-align: center; }
        .nav { display: flex; justify-content: center; background-color: #333; }
        .nav a { color: white; padding: 14px 20px; text-decoration: none; text-align: center; }
        .nav a:hover { background-color: #ddd; color: black; }
        .container { margin: 20px auto; padding: 20px; max-width: 800px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        .section { margin-bottom: 20px; }
        h1, h2 { margin-top: 0; }
        .button { background-color: #4CAF50; border: none; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 4px; }
        .button:hover { background-color: #45a049; }

    </style>

</head>

<body>
    <div class="header"><h1>Metaverso Crypto 3D</h1></div>
    <div class="nav">

        <a href="#">metaverso</a>
        <a href="#usuarios">Usuarios</a>
        <a href="#recursos">Recursos</a>
        <a href="#blockchain">Blockchain</a>
        <a href="#database">Base de Datos</a>
        <a href="#compresion">Compresión</a>
        <a href="#servidor">Servidor</a>

    </div>
    <div class="container">
        <div id="home" class="section">
            <h2>Entorno 3D</h2>
            <div id="unityContainer" style="width: 960px; height: 600px"></div>
            <script>
                var buildUrl = "{{ url_for('static', filename='unity/Build') }}";
                var loaderUrl = buildUrl + "/{{ 'Build.loader.js' }}";
                var config = {
                    dataUrl: buildUrl + "/{{ 'Build.data' }}",
                    frameworkUrl: buildUrl + "/{{ 'Build.framework.js' }}",
                    codeUrl: buildUrl + "/{{ 'Build.wasm' }}",
                    streamingAssetsUrl: "StreamingAssets",
                    companyName: "DefaultCompany",
                    productName: "MyProduct",
                    productVersion: "0.1",
                };

                var container = document.querySelector("#unityContainer");
                var canvas = document.createElement("canvas");
                container.appendChild(canvas);

                var script = document.createElement("script");
                script.src = loaderUrl;
                script.onload = () => {
                    createUnityInstance(canvas, config, (progress) => {
                        console.log(progress);
                    }).then((unityInstance) => {
                        console.log("Unity instance created");
                    }).catch((message) => {
                        console.error(message);
                    });
                };
                document.body.appendChild(script);
            </script>
        </div>
    </div>
    En desarrollo, un metaverso crypto 3D descentralizado.
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    
