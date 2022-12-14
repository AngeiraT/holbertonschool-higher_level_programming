#!/usr/bin/node

let start = 0;

exports.esrever = function (list) {
    
    let end = list.length - 1;
    const arr = [...list];
  
    for (; start < list.length; start++) {
      arr[start] = list[end];
      end--;
    }
  
    return arr;
  };
