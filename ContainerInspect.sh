if [ "$( docker container inspect -f '{{.State.Running}}' AlpCon )" == "true" ]; then
	echo "AlpCon running, starting Python script"
else
	echo "AlpCon not running, starting AlpCon"
	docker rm -f AlpCon
	docker run -it --name AlpCon alpcon
fi
