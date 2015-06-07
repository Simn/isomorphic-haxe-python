class Client {
  public static function main() {
    var template = new Template();
    template.title="Hello for client side";
    template.body="This content is rendered in javascript";
    js.Browser.document.getElementById('content').innerHTML = template.execute();
  }
}
