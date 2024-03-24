import pandas as pd
import companyMod as cm
from companyMod import ( 
    Hotel as cmh, 
    Trade as cmt, 
    Agriculture as cma, 
    ServiceSector as cms, 
    Manuf as cmm, 
    mining_forestry as cmmf
)

def series_ratios_trade(in_obj):
    list_ratios = [
        in_obj.date_record
        , cmt.inv_trnovr(in_obj), cmt.days_sales_inv_trnovr(in_obj)
        , cmt.current_ratio(in_obj), cmt.quick_ratio(in_obj), cmt.cash_ratio(in_obj)
        , cmt.total_debt_ratio(in_obj), cmt.dept_equity_ratio(in_obj), cmt.equity_multi(in_obj), cmt.tie(in_obj), cmt.cash_cov_ratio(in_obj)
        , cmt.rece_trnovr(in_obj), cmt.days_sales_rece_trnover(in_obj), cmt.total_asset_trnovr(in_obj)
        , cmt.profit_marg(in_obj), cmt.return_assets(in_obj), cmt.return_equity(in_obj), cmt.wages_rev_ratio(in_obj)
    ]
    series_ratios = pd.Series(list_ratios, index = ['date_record', 'inv_trnovr', 'days_sales_inv_trnovr', 'current_ratio', 'quick_ratio', 'cash_ratio', 'total_debt_ratio', 'dept_equity_ratio', 'equity_multi', 'tie', 'cash_cov_ratio', 'rece_trnovr', 'days_sales_rece_trnover', 'total_asset_trnovr', 'profit_marg', 'return_assets', 'return_equity', 'wages_rev_ratio'])
    return series_ratios    

def series_ratios_hotel(in_obj):
    list_ratios = [
        cmh.date_record
        , cmh.occ_rate(in_obj), cmh.ave_daily_rate(in_obj), cmh.rev_per_room_aval(in_obj), cmh.GOPPAR(in_obj), cmh.rev_par(in_obj)
        , cmh.current_ratio(in_obj), cmh.quick_ratio(in_obj), cmh.cash_ratio(in_obj)
        , cmh.total_debt_ratio(in_obj), cmh.dept_equity_ratio(in_obj), cmh.equity_multi(in_obj), cmh.tie(in_obj), cmh.cash_cov_ratio(in_obj)
        , cmh.rece_trnovr(in_obj), cmh.days_sales_rece_trnover(in_obj), cmh.total_asset_trnovr(in_obj)
        , cmh.profit_marg(in_obj), cmh.return_assets(in_obj), cmh.return_equity(in_obj), cmh.wages_rev_ratio(in_obj)
    ]
    series_ratios = pd.Series(list_ratios, index=['date_record', 'occ_rate', 'ave_daily_rate', 'rev_per_room_aval', 'GOPPAR', 'rev_par', 'current_ratio', 'quick_ratio', 'cash_ratio', 'total_debt_ratio', 'dept_equity_ratio', 'equity_multi', 'tie', 'cash_cov_ratio', 'rece_trnovr', 'days_sales_rece_trnover', 'total_asset_trnovr', 'profit_marg', 'return_assets', 'return_equity', 'wages_rev_ratio'])
    return series_ratios

def series_ratios_agriculture(in_obj):
    list_ratios = [
        cma.date_record
        , cma.land_yield(in_obj), cma.livestock_yield(in_obj)
        , cma.current_ratio(in_obj), cma.quick_ratio(in_obj), cma.cash_ratio(in_obj)
        , cma.total_debt_ratio(in_obj), cma.dept_equity_ratio(in_obj), cma.equity_multi(in_obj), cma.tie(in_obj), cma.cash_cov_ratio(in_obj)
        , cma.rece_trnovr(in_obj), cma.days_sales_rece_trnover(in_obj), cma.total_asset_trnovr(in_obj)
        , cma.profit_marg(in_obj), cma.return_assets(in_obj), cma.return_equity(in_obj), cma.wages_rev_ratio(in_obj)
    ]
    series_ratios = pd.Series(list_ratios, index=['date_record', 'land_yield', 'livestock_yield', 'current_ratio', 'quick_ratio', 'cash_ratio', 'total_debt_ratio', 'dept_equity_ratio', 'equity_multi', 'tie', 'cash_cov_ratio', 'rece_trnovr', 'days_sales_rece_trnover', 'total_asset_trnovr', 'profit_marg', 'return_assets', 'return_equity', 'wages_rev_ratio'])
    return series_ratios

def series_ratios_service_sector(in_obj):
    list_ratios = [
        cms.date_record
        , cms.profit_marg_partner(), cms.fee_rev_consultant_ratio()
        , cms.current_ratio(in_obj), cms.quick_ratio(in_obj), cms.cash_ratio(in_obj)
        , cms.total_debt_ratio(in_obj), cms.dept_equity_ratio(in_obj), cms.equity_multi(in_obj), cms.tie(in_obj), cms.cash_cov_ratio(in_obj)
        , cms.rece_trnovr(in_obj), cms.days_sales_rece_trnover(in_obj), cms.total_asset_trnovr(in_obj)
        , cms.profit_marg(in_obj), cms.return_assets(in_obj), cms.return_equity(in_obj), cms.wages_rev_ratio(in_obj)
    ]
    series_ratios = pd.Series(list_ratios, index=['date_record', 'profit_marg_partner', 'fee_rev_consultant_ratio', 'current_ratio', 'quick_ratio', 'cash_ratio', 'total_debt_ratio', 'dept_equity_ratio', 'equity_multi', 'tie', 'cash_cov_ratio', 'rece_trnovr', 'days_sales_rece_trnover', 'total_asset_trnovr', 'profit_marg', 'return_assets', 'return_equity', 'wages_rev_ratio'])
    return series_ratios

def series_ratios_manuf(in_obj):
    list_ratios = [
        cmm.date_record
        , cmm.inv_trnovr(), cmm.manuf_cost_exp_ratio(), cmm.mtrils_cost_exp_ratio()
        , cmm.current_ratio(in_obj), cmm.quick_ratio(in_obj), cmm.cash_ratio(in_obj)
        , cmm.total_debt_ratio(in_obj), cmm.dept_equity_ratio(in_obj), cmm.equity_multi(in_obj), cmm.tie(in_obj), cmm.cash_cov_ratio(in_obj)
        , cmm.rece_trnovr(in_obj), cmm.days_sales_rece_trnover(in_obj), cmm.total_asset_trnovr(in_obj)
        , cmm.profit_marg(in_obj), cmm.return_assets(in_obj), cmm.return_equity(in_obj), cmm.wages_rev_ratio(in_obj)
    ]
    series_ratios = pd.Series(list_ratios, index=['date_record', 'inv_trnovr', 'manuf_cost_exp_ratio', 'mtrils_cost_exp_ratio', 'current_ratio', 'quick_ratio', 'cash_ratio', 'total_debt_ratio', 'dept_equity_ratio', 'equity_multi', 'tie', 'cash_cov_ratio', 'rece_trnovr', 'days_sales_rece_trnover', 'total_asset_trnovr', 'profit_marg', 'return_assets', 'return_equity', 'wages_rev_ratio'])
    return series_ratios

def series_ratios_mining_forestry(in_obj):
    list_ratios = [
        cmmf.date_record
        , cmmf.total_debt_ratio(), cmmf.equity_multi(), cmmf.total_asset_trnovr(), cmmf.return_assets(), cmmf.cash_cov_ratio()
        , cmmf.current_ratio(in_obj), cmmf.quick_ratio(in_obj), cmmf.cash_ratio(in_obj)
        , cmmf.total_debt_ratio(in_obj), cmmf.dept_equity_ratio(in_obj), cmmf.equity_multi(in_obj), cmmf.tie(in_obj), cmmf.cash_cov_ratio(in_obj)
        , cmmf.rece_trnovr(in_obj), cmmf.days_sales_rece_trnover(in_obj), cmmf.total_asset_trnovr(in_obj)
        , cmmf.profit_marg(in_obj), cmmf.return_assets(in_obj), cmmf.return_equity(in_obj), cmmf.wages_rev_ratio(in_obj)
    ]
    series_ratios = pd.Series(list_ratios, index=['date_record', 'total_debt_ratio', 'equity_multi', 'total_asset_trnovr', 'return_assets', 'cash_cov_ratio', 'current_ratio', 'quick_ratio', 'cash_ratio', 'total_debt_ratio', 'dept_equity_ratio', 'equity_multi', 'tie', 'cash_cov_ratio', 'rece_trnovr', 'days_sales_rece_trnover', 'total_asset_trnovr', 'profit_marg', 'return_assets', 'return_equity', 'wages_rev_ratio'])
    return series_ratios