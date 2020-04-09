#coding=utf-8

import configparser
import codecs

class ReadConfig:
    """
    专门读取配置文件的，.ini文件格式
    """
    def __init__(self, filename):
        # configpath = os.path.join(prjDir,filename)
        configpath = filename
        # print(configpath)
        fd = open(configpath)
        data = fd.read()
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def getValue(self, env, name):
        """
        [projectConfig]
        project_path=E:/Python-Project/UItestframework
        :param env:[projectConfig]
        :param name:project_path
        :return:E:/Python-Project/UItestframework
        """
        return self.cf.get(env,name)


if __name__ == "__main__":
    filename = "D:\\oneDrive\\Test\\UItestframework-master\\config\\config.ini"
    configpath = filename
    # print(configpath)

    fd = open(configpath)
    data = fd.read()
    print(filename)
    print(codecs.BOM_UTF8)
    print(type(data))
    print(data)
    print(data[:3])
    print(data[3:])

    cf = configparser.ConfigParser()
    cf.read(configpath)
