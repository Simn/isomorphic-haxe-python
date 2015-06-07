import haxe.Constraints.Function;
import python.KwArgs;
using python.Lib;


@:pythonImport("flask", "request")
  extern class Request implements Dynamic {
  public static var args:python.Dict<String,Dynamic>;
}


@:pythonImport("flask", "Flask")
extern class Flask {
  function new(module:String);
  function run(?opts:KwArgs<{?debug:Bool}>):Void;
  function route<T:Function>(path:String, ?opts:KwArgs<{?defaults:Dynamic}>):T->T;
}

class Server {
  public static function main() {

   var app = new Flask(untyped __name__);
   app.route("/server")(serverSide);
   app.route("/client")(clientSide);
   app.run();
  }


  static function clientSide() {
    return '
      <html>
        <body>
         <div id="content"></div>
          <script src="static/js/client.js"></script>
        </body>
      </html>

    ';
  }

  static function serverSide() {
    var template = new Template();
    template.title = "Hello from server side";
    template.body = "This content is rendered in python";
    return template.execute();
  }

}
