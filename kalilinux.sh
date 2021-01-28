clear
    printf "${blue}{SEA}##################################################{SEA}\n"
    printf "${blue}##                                              ##\n"
    printf "${blue}##  88      a8P         db        88        88  ##\n"
    printf "${blue}##  88    .88'         d88b       88        88  ##\n"
    printf "${blue}##  88   88'          d8''8b      88        88  ##\n"
    printf "${blue}##  88 d88           d8'  '8b     88        88  ##\n"
    printf "${blue}##  8888'88.        d8YaaaaY8b    88        88  ##\n"
    printf "${blue}##  88P   Y8b      d8''''''''8b   88        88  ##\n"
    printf "${blue}##  88     '88.   d8'        '8b  88        88  ##\n"
    printf "${blue}##  88       Y8b d8'          '8b 888888888 88  ##\n"
    printf "${blue}##                           THE SEA                                  ##\n"
    printf "${blue}{SEA}####  ############# NetHunter ####################{SEA}${reset}\n\n"
printf "                                        \e[1;77m VOLCANO963 \e[0m \n"
printf "\e[1;77m v2.0 SEA \e[0m \n"
printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m01\e[0m\e[1;92m]\e[0m\e[1;93m kalilinux nethunter\e[0m"  ; printf "                   \e[1;92m[\e[0m\e[1;77m02\e[0m\e[1;92m]\e[0m\e[1;93m kali.sh\e[0m\n"

read -p $'\n\e[1;92m[\e[0m\e[1;77mSEA\e[0m\e[1;92m] Enter the number : \e[0m' name 
if [ "$name" = "1" ] ; then 
      termux-setup-storage
      pkg install wget
      chmod +x kalilinux-nethunter
     ./kalilinux-nethunter

elif [ "$name" = "2" ] ; then 
    cd $HOME
    mkdir kali;cd kali;pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh
   ./start.sh
    
else 
     bash Aminosploit.sh
fi