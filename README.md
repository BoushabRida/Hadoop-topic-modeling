# Hadoop-topic-modeling
Finding the topic of files with the MapReduce which is a processing technique and a program model for distributed computing based on java. The MapReduce algorithm contains two important tasks, namely Map and Reduce. Map takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key/value pairs). Secondly, reduce task, which takes the output from a map as an input and combines those data tuples into a smaller set of tuples. As the sequence of the MapReduce implies, the reduce task is always performed after the map job

The file Map.py gonna map our data from the texts data (text1,2,3 and 4)
then we gonna reuce to find the topic of the file.

there's two ways to run this:
with HadoopEmulateurScratch build from scratch you need to passe three arguments after call it which they are -map.py -reduce.py -input

Or  in (Cloudea) VM by starting Hadoop ecosystem.

Thanks for reading !

Happy githubing!
