def delete_line(stringToMatch, file_in, interactive=False, backup=False):
    from rm_known_host.backup import backup_function
    print(f"Remove {stringToMatch} from {file_in}")
    output = []
    counter = 0
    with open(file_in) as oldfile:
        for line in oldfile:
            if not stringToMatch in line:
                output.append(line)
            else:
                counter += 1
    
    confirm = 'Y'
    if counter == 0:
        print(f"String {stringToMatch} was not found!")

    if interactive and counter > 0:
        confirm = input(f"The known_host file has {counter} matches to {stringToMatch} Continue(Y/N): ")
    
    if confirm.upper() == 'Y' and counter > 0:
        if backup:
            backup_function()

        file_out = open(file_in, 'w')
        file_out.writelines(output)
        file_out.close()

        print(f"Removed lines containing {stringToMatch} from {file_in}.")
        

# delete_line('18.2', '/home/cloud_user/.ssh/known_hosts', True)