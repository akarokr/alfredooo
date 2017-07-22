## What is Alfredooo?
Alfredooo is the new CI tool, made by a lazy developer. With Alfredooo you just add your pipeline.yml file and boom, call him: "ALFREDOOOO".


## Why the name?
Well, click [here](https://www.youtube.com/watch?v=iIsANBIa-JI).

## How to use
You need a YML file to set your tasks, the script will read them and execute the commands described also in the file. After you set all the tasks and commands, execute him.

```
$ alfredooo.py -p <PIPELINE_FILE> -u <GIT_URL
```

### YML file format
The pipeline file has only three main hashes.
- Branch: Repository branch that should be used to execute the code.
- Tasks: Saved commands that can be used to create a pipeline
- Pipelines: Group of ordered tasks

Example:

```yml
# Tasks should be execute from this branch
branch: <BRANCH NAME>

#Things a wanna execute
tasks:
  - <SOME NAME>:
      cmd: <COMMANDS>

# Ordenaded way to run my steps
pipelines:
  - <NOME NAME>:
     - <TASK NAME>
```
