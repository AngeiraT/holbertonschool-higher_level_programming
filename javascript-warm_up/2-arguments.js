#!/usr/bin/node

/* To keep in mind, process.argv[0] is the #!/usr/bin/node,
but it is kept "hidden" so what you count in the command line
starts from 1 (the executable) and so on.
*/

if (process.argv.lenght === 3) {
    console.log('Argument found');
  } else if (process.argv.lenght >= 4) {
    console.log('Arguments found');
  } else {
    console.log('No argument');
  }
