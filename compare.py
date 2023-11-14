import git
from xml.etree import ElementTree as ET

def compare_xml_files(repo_path, file1_path, file2_path):
    # Open the Git repository
    repo = git.Repo(repo_path)

    # Get the commits that modified the given files
    commits_file1 = list(repo.iter_commits(paths=file1_path))
    commits_file2 = list(repo.iter_commits(paths=file2_path))

    # Get the content of the files in the latest commit
    latest_content_file1 = commits_file1[0].tree[file1_path].data_stream.read()
    latest_content_file2 = commits_file2[0].tree[file2_path].data_stream.read()

    # Parse XML content
    xml_tree_file1 = ET.fromstring(latest_content_file1)
    xml_tree_file2 = ET.fromstring(latest_content_file2)

    # Compare the content of the XML trees
    if ET.tostring(xml_tree_file1) != ET.tostring(xml_tree_file2):
        print(f"Changes detected between {file1_path} and {file2_path}.")

        # You can further customize the comparison or output here
        print("Unified Diff is not directly applicable to XML, so you may want to implement custom logic.")

    else:
        print(f"No changes between {file1_path} and {file2_path}.")

# Example usage:
compare_xml_files('/Users/christineliu/Dropbox (MIT)/Personal/Research ideas/Export control/EAR', '2023.10.18.xml', '2023.10.25.xml')
