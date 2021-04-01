from factortest.Infras.Contract import Contract
from factortest.Infras.base_para import *
from factortest.Infras.TradeCalender import TradeCalender


class FactorRoughTest:
    def __init__(self, contract_info_list, local_data_path):
        self.contract_dict = self._gen_contract(contract_info_list=contract_info_list)
        self.trade_calender = TradeCalender(local_data_path=local_data_path)

    def _gen_contract(self, contract_info_list) -> dict:
        contract_dict = {}
        for contract in contract_info_list:

            contract_dict[contract['id']] = Contract(
                commodity=contract['id'],
                first_listed_date=contract['first_listed_date'],
                month_list=contract['month_list'],
                init_margin_rate=contract['init_margin_rate'],
                contract_unit=contract['contract_unit'],
                open_comm=contract['open_comm'],
                close_comm=contract['close_comm'],
            )

        return contract_dict

    def all_commodity_main_contract(self) -> list:
        # 选择样本空间
        # 所有商品的主力合约
        pass

    def all_commodity_all_feasible_contract(self) -> list:
        # 选择样本空间
        # 所有商品的主力和次主力合约
        pass

    def factor_ic(self, factor, contract_space):
        # 在给定合约样本空间内计算每个截面的IC和ICIR
        # 画图
        pass

if __name__ == '__main__':
    factor_rough_test = FactorRoughTest(
        contract_info_list=FULL_CONTRACT_INFO,
        local_data_path=LOCAL_DATA_PATH
    )