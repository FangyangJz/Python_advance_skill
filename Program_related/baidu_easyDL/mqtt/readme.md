
docker pull emqx/emqx
docker run -d --name emqx31 -p 1883:1883 -p 8083:8083 -p 8883:8883 -p 8084:8084 -p 18083:18083 emqx/emqx:v4.0.2


######

service docker start // 启动docker
docker ps -l 列出容器
1.启动容器，命令：docker start 容器ID或容器名
2.重启容器，命令：docker restart 容器ID或容器名
3.停止容器，命令：docker stop 容器ID或容器名
4.强制停止容器，命令：docker kill 容器ID或容器名

########################################
tmux new -s mqtt  //新建session
tmux ls
tmux attach -t mqtt 
ctrl+b -> d  //离开