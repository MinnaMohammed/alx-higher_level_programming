#!usr/bin/node
exports.logMe = function (item) {
  let argsCnt = 0;
  for (let i = 2; i < process.argv.length; i++) {
    console.log(argsCnt + ': ' + process.argv[i]);
    argsCnt++;
  }
};
