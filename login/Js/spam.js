const thrift = require('thrift-http');
const LineService = require('LineService');

var _client = '';
var gid = '';
var uids = [];
var token = ''; 

process.argv.forEach(function (val) {
  if(val.includes('name=')){
    gid = val.split('name=').pop();
  }else if(val.includes('uid=')){
    uids.push(val.split('uid=').pop());
  }else if(val.includes('token=')){
    token = val.split('token=').pop();
  }
});

function setTHttpClient(options) {
    var connection =
      thrift.createHttpConnection('legy-jp.line.naver.jp', 443, options);
    connection.on('error', (err) => {
      console.log('err',err);
      return err;
    });
    _client = thrift.createHttpClient(LineService, connection);
  }
  
  
setTHttpClient(options={
    protocol: thrift.TCompactProtocol,
    transport: thrift.TBufferedTransport,
    headers: {'User-Agent':'Line/8.9.0','X-Line-Application':"IOSIPAD\t11.2.5\tiPhone X\t11.2.5",'X-Line-Access':token},
    path: '/S4',
    https: true
    });

for (var i=0; i < 3000; i++) {
   _client.createGroup(0, gid, uids);
}