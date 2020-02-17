
def delete_line(stringToMatch, file_in):
    print(f"Remove {stringToMatch} from {file_in}")
    output = []
    counter = 0
    with open(file_in) as oldfile:
        for line in oldfile:
            if not stringToMatch in line:
                output.append(line)
            else:
                counter += 1


    if counter > 0:
        file_out = open(file_in, 'w')
        file_out.writelines(output)
        file_out.close()
    else:
        print(f"String {stringToMatch} was not found!")


delete_line('3.9', '/home/cloud_user/.ssh/known_hosts')

#new_output = open()