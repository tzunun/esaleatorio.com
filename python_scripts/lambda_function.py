import json
import boto3
from datetime import datetime

"""
codebuild will have have to delete the posts after building the site,
that way this lambda function will not spend time deleting the files, only
writting the new ones and pushing those files to the repo.

"""
repository_name = 'esaleatorio'
commit_message = 'Pushed from AWS Lambda to CodeCommit'
folder_path = 'content/'
test_file = "Ramdom text from AWS Lamda, Test 2!"
branch_name = 'master'
    
def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('codecommit')
    response = client.get_folder(repositoryName=repository_name, folderPath=folder_path)
    keys = response['files']
    commit_id = response['commitId']

        
    delete_files = []
    for key in keys:
        delete_files.append({'filePath': key.get('absolutePath')})
        
    #commit_response = client.create_commit(
    #    repositoryName=repository_name,
    #    branchName=branch_name,
    #    parentCommitId=commit_id,
    #    authorName='Antonio Hernandez',
    #    email='antonio@mlmusings.com',
    #    commitMessage='Deleted previous posts.',
    #    keepEmptyFolders=True,
    #    deleteFiles = delete_files
    #    )
        
        
        #commit_response = client.put_file(
        #    repositoryName=repository_name,
        #    branchName=branch_name,
        #    fileContent=str.encode(test_file),
        #    filePath='/content/posts/aws_text_file',
        #    parentCommitId=commit_id,
        #    commitMessage=commit_message,
        #    name='Antonio Hernandez'
        #    )#
