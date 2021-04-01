import pandas as pd

pd.set_option('expand_frame_repr', False)

class AbsFactor:
    def __init__(self, base_data_freq, pred_freq):
        pass

    def cal_factor(self):
        pass

    def save_data(self):
        pass

    def single_contract_test(self, contract_list):
        """
        该因子对选中的单个合约测试
        :param contract_list:
        :return:
        """
        pass

    def sample_test(self, contract_list):
        """
        该因子对某一个截面的合约进行测试
        :param contract_list:
        :return:
        """
        pass


class Std(AbsFactor):
    def __init__(self, base_para_freq, pred_freq):
        AbsFactor.__init__(self, base_para_freq, pred_freq)




