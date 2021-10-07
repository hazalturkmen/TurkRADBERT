import glob
import re
from tqdm import tqdm


def preproc(sentence):
    """

    :param sentence:
    :return:sentece
    """
    sentence = sentence.strip()
    #sentence = sentence.lower()
    punc = '''!()-[]{};:'"\,<>./?@$%^&±*_~'''
    sentence = re.sub("[0-9]", "#", sentence)
    for ele in sentence:
        if ele in punc:
            sentence = sentence.replace(ele, "")
    return sentence


def preproc_files():
    files = glob.glob("/home/hazal/nlp_dataset/brain_CT/splitted_txt_2/*.txt")
    print("\nPre-processing medical text...")
    with open('/home/hazal/nlp_dataset/brain_CT/tr_medical_processed', 'w') as fo:
        for f in tqdm(files):
            f_txt = open(f, "r")
            file_contents = f_txt.read()
            contents_split = file_contents.splitlines()
            for sent in contents_split:
                fo.write(preproc(sent))
                fo.write("\n")
    fo.close()


def preproc_single_file():
    print("\nPre-processing medical text...")
    with open('/home/hazal/nlp_dataset/brain_CT/tr_medical_data/tr_articles_processed.txt', 'w') as fo:
        f_txt = open("/home/hazal/nlp_dataset/brain_CT/tr_medical_data/tr_articles_2.txt", "r")
        file_contents = f_txt.read()
        contents_split = file_contents.splitlines()
        for sent in contents_split:
            fo.write(preproc(sent))
            fo.write("\n")
    fo.close()
    f_txt.close()



if __name__ == '__main__':
    preproc_single_file()
