system("clear")
   puts " {SEA}##################################################{SEA}\n"
   puts " ##                                              ##\n"
   puts " ##  88      a8P         db        88        88  ##\n"
   puts " ##  88    .88'         d88b       88        88  ##\n"
   puts " ##  88   88'          d8''8b      88        88  ##\n"
   puts " ##  88 d88           d8'  '8b     88        88  ##\n"
   puts " ##  8888'88.        d8YaaaaY8b    88        88  ##\n"
   puts " ##  88P   Y8b      d8''''''''8b   88        88  ##\n"
   puts " ##  88     '88.   d8'        '8b  88        88  ##\n"
   puts " ##  88       Y8b d8'          '8b 888888888 88  ##\n"
   puts " ##                           THE SEA                                  ##\n"
   puts " {SEA}####  ############# NetHunter ####################{SEA}\n\n"
puts "                             VOLCANO963  \n"
puts "                                SEA  \n"
puts "    [1]kalilinux nethunter"  ; puts "   [2]kali.sh\n"

puts("\n\n\n       [SEA]Enter The Number:")
FACK=gets.chomp.to_i
 if FACK ==1
    system("termux-setup-storage") 
    system("pkg install wget") 
    system("chmod +x kalilinux-nethunter") 
    system("./kalilinux-nethunter") 
 elsif FACK ==2
    system("cd $HOME") 
    system("mkdir kali;cd kali;pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh") 
   system("./start.sh") 
 else
   puts "fack you and fack the number"
   system("bash Aminosploit.sh") 
 end
