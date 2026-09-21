#!/bin/bash
shopt -s nocasematch

AI_item=""
win_limit=2
player_wins="0"
AI_wins="0"

read -p "Before we begin, decide how many times one must win to win the series" limit
	win_limit=$limit 

echo -e "You have disrecpected me for the last time!!! \n Its time for rock paper scissors!"

sleep 2
enemy_choice(){
	local index=$((RANDOM % 3 + 1))
	case $index in
	1)
		AI_item="rock"
		;;
	
	2) AI_item="paper"
		;;
	
	3)
		AI_item="scissors"
		;;
	esac

}

current_score(){
	echo "Your wins: $player_wins"
	echo "John's wins: $AI_wins"

	sleep 2
}

while (( player_wins < win_limit && AI_wins < win_limit)); do
	read -p "Choose your item: (rock, paper, scissors)" rps_choice

if [[ ! $rps_choice =~ ^(rock|paper|scissors)$ ]]; then
	echo "rock, paper and scissors are your only options here."
	continue
fi

enemy_choice

echo -e "I choose $AI_item"
sleep 2



	if [[ $rps_choice == "rock" && $AI_item == "scissors" ]]; then
		echo "You are up one!"
		player_wins=$((player_wins + 1 ))
		sleep 1
		current_score

	elif [[ $rps_choice == "paper" && $AI_item == "rock" ]]; then
		echo "You are up one!"
		player_wins=$((player_wins + 1 ))
		sleep 1
		current_score
	
	elif [[ $rps_choice == "scissors" && $AI_item == "paper" ]]; then
		echo "You are up one!"
		player_wins=$((player_wins + 1 ))
		sleep 1
		current_score

	elif [[ $rps_choice == $AI_item ]]; then
		echo "A tie! No points awarded"
		sleep 1
		current_score

	else
		echo "You lost, John gains one point."
		AI_wins=$(( AI_wins + 1 ))
		sleep 1
		current_score

	fi 

	if [[ $player_wins == $win_limit ]]; then
		echo "You get a one time free pass to cut elinore's hair"
	fi

	if [[ $AI_wins == $win_limit ]]; then
		echo "No the bot was not rigged you just suck"
	fi

done