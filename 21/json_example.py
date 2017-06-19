import json

if __name__ == '__main__':

    with open('content.json', 'r') as f:
        read_dict = json.load(f)

    print read_dict
    print "The password was"
    print read_dict['related_content']['passphrase']




