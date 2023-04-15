from django.db import models

class BankBranch(models.Model):
    rssd_id_branch = models.IntegerField(db_column='RSSD ID Branch', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rssd_id_hq = models.IntegerField(db_column='RSSD ID HQ')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    branch = models.CharField(db_column='Branch', max_length=30, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=40, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=25, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bank_branch'


class BankData(models.Model):
    rssd_id = models.IntegerField(db_column='RSSD ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period = models.DateField(db_column='Period')  # Field name made lowercase.
    updated = models.DateTimeField(db_column='Updated')  # Field name made lowercase.
    residential_first_total = models.IntegerField(db_column='Residential First Total', blank=True, null=True)
    residential_first_charge_offs_ytd = models.IntegerField(db_column='Residential First Charge-offs YTD', blank=True, null=True)
    residential_first_recoveries_ytd = models.IntegerField(db_column='Residential First Recoveries YTD', blank=True, null=True)
    residential_first_30day = models.IntegerField(db_column='Residential First 30Day', blank=True, null=True)
    residential_first_30day_of_total = models.IntegerField(db_column='Residential First 30Day Pct of Total', blank=True, null=True)
    residential_first_30day_pg_pctl = models.IntegerField(db_column='Residential First 30Day PG PCTL', blank=True, null=True)
    residential_first_90day = models.IntegerField(db_column='Residential First 90Day', blank=True, null=True)
    residential_first_90day_of_total = models.IntegerField(db_column='Residential First 90Day Pct of Total', blank=True, null=True)
    residential_first_90day_pg_pctl = models.IntegerField(db_column='Residential First 90Day PG PCTL', blank=True, null=True)
    residential_first_nonaccrual_balance = models.IntegerField(db_column='Residential First Nonaccrual Balance', blank=True, null=True)
    residential_first_nonaccrual_of_total = models.IntegerField(db_column='Residential First Nonaccrual Pct of Total', blank=True, null=True)
    residential_first_nonaccrual_pg_pctl = models.IntegerField(db_column='Residential First Nonaccrual PG PCTL', blank=True, null=True)
    residential_first_nonaccrual_qtr_chg_field = models.IntegerField(db_column='Residential First Nonaccrual Qtr Chg $', blank=True, null=True)
    residential_first_nonaccrual_qtr_chg_field_0 = models.IntegerField(db_column='Residential First Nonaccrual Qtr Chg Pct', blank=True, null=True)
    residential_first_nonaccrual_yr_chg_field = models.IntegerField(db_column='Residential First Nonaccrual Yr Chg $', blank=True, null=True)
    residential_first_nonaccrual_yr_chg_field_0 = models.IntegerField(db_column='Residential First Nonaccrual Yr Chg Pct', blank=True, null=True)
    residential_jr_total = models.IntegerField(db_column='Residential Jr Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    residential_jr_charge_offs_ytd = models.IntegerField(db_column='Residential Jr Charge-offs YTD', blank=True, null=True)
    residential_jr_recoveries_ytd = models.IntegerField(db_column='Residential Jr Recoveries YTD', blank=True, null=True)
    residential_jr_30day = models.IntegerField(db_column='Residential Jr 30Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    residential_jr_30day_of_total = models.IntegerField(db_column='Residential Jr 30Day Pct of Total', blank=True, null=True)
    residential_jr_30day_pg_pctl = models.IntegerField(db_column='Residential Jr 30Day PG PCTL', blank=True, null=True)
    residential_jr_90day = models.IntegerField(db_column='Residential Jr 90Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    residential_jr_90day_of_total = models.IntegerField(db_column='Residential Jr 90Day Pct of Total', blank=True, null=True)
    residential_jr_90day_pg_pctl = models.IntegerField(db_column='Residential Jr 90Day PG PCTL', blank=True, null=True)
    residential_jr_nonaccrual_balance = models.IntegerField(db_column='Residential Jr Nonaccrual Balance', blank=True, null=True)
    residential_jr_nonaccrual_of_total = models.IntegerField(db_column='Residential Jr Nonaccrual Pct of Total', blank=True, null=True)
    residential_jr_nonaccrual_pg_pctl = models.IntegerField(db_column='Residential Jr Nonaccrual PG PCTL', blank=True, null=True)
    residential_jr_nonaccrual_qtr_chg_field = models.IntegerField(db_column='Residential Jr Nonaccrual Qtr Chg $', blank=True, null=True)
    residential_jr_nonaccrual_qtr_chg_field_0 = models.IntegerField(db_column='Residential Jr Nonaccrual Qtr Chg Pct', blank=True, null=True)
    residential_jr_nonaccrual_yr_chg_field = models.IntegerField(db_column='Residential Jr Nonaccrual Yr Chg $', blank=True, null=True)
    residential_jr_nonaccrual_yr_chg_field_0 = models.IntegerField(db_column='Residential Jr Nonaccrual Yr Chg Pct', blank=True, null=True)
    residential_heloc_total = models.IntegerField(db_column='Residential HELOC Total', blank=True, null=True)
    residential_heloc_charge_offs_ytd = models.IntegerField(db_column='Residential HELOC Charge-offs YTD', blank=True, null=True)
    residential_heloc_recoveries_ytd = models.IntegerField(db_column='Residential HELOC Recoveries YTD', blank=True, null=True)
    residential_heloc_30day = models.IntegerField(db_column='Residential HELOC 30Day', blank=True, null=True)
    residential_heloc_30day_of_total = models.IntegerField(db_column='Residential HELOC 30Day Pct of Total', blank=True, null=True)
    residential_heloc_30day_pg_pctl = models.IntegerField(db_column='Residential HELOC 30Day PG PCTL', blank=True, null=True)
    residential_heloc_90day = models.IntegerField(db_column='Residential HELOC 90Day', blank=True, null=True)
    residential_heloc_90day_of_total = models.IntegerField(db_column='Residential HELOC 90Day Pct of Total', blank=True, null=True)
    residential_heloc_90day_pg_pctl = models.IntegerField(db_column='Residential HELOC 90Day PG PCTL', blank=True, null=True)
    residential_heloc_nonaccrual_balance = models.IntegerField(db_column='Residential HELOC Nonaccrual Balance', blank=True, null=True)
    residential_heloc_nonaccrual_of_total = models.IntegerField(db_column='Residential HELOC Nonaccrual Pct of Total', blank=True, null=True)
    residential_heloc_nonaccrual_pg_pctl = models.IntegerField(db_column='Residential HELOC Nonaccrual PG PCTL', blank=True, null=True)
    residential_heloc_nonaccrual_qtr_chg_field = models.IntegerField(db_column='Residential HELOC Nonaccrual Qtr Chg $', blank=True, null=True)
    residential_heloc_nonaccrual_qtr_chg_field_0 = models.IntegerField(db_column='Residential HELOC Nonaccrual Qtr Chg Pct', blank=True, null=True)
    residential_heloc_nonaccrual_yr_chg_field = models.IntegerField(db_column='Residential HELOC Nonaccrual Yr Chg $', blank=True, null=True)
    residential_heloc_nonaccrual_yr_chg_field_0 = models.IntegerField(db_column='Residential HELOC Nonaccrual Yr Chg Pct', blank=True, null=True)
    construction_resi_total = models.IntegerField(db_column='Construction Resi Total', blank=True, null=True)
    construction_resi_charge_offs_ytd = models.IntegerField(db_column='Construction Resi Charge-offs YTD', blank=True, null=True)
    construction_resi_recoveries_ytd = models.IntegerField(db_column='Construction Resi Recoveries YTD', blank=True, null=True)
    construction_resi_30day = models.IntegerField(db_column='Construction Resi 30Day', blank=True, null=True)
    construction_resi_30day_of_total = models.IntegerField(db_column='Construction Resi 30Day Pct of Total', blank=True, null=True)
    construction_resi_30day_pg_pctl = models.IntegerField(db_column='Construction Resi 30Day PG PCTL', blank=True, null=True)
    construction_resi_90day = models.IntegerField(db_column='Construction Resi 90Day', blank=True, null=True)
    construction_resi_90day_of_total = models.IntegerField(db_column='Construction Resi 90Day Pct of Total', blank=True, null=True)
    construction_resi_90day_pg_pctl = models.IntegerField(db_column='Construction Resi 90Day PG PCTL', blank=True, null=True)
    construction_resi_nonaccrual_balance = models.IntegerField(db_column='Construction Resi Nonaccrual Balance', blank=True, null=True)
    construction_resi_nonaccrual_of_total = models.IntegerField(db_column='Construction Resi Nonaccrual Pct of Total', blank=True, null=True)
    construction_resi_nonaccrual_pg_pctl = models.IntegerField(db_column='Construction Resi Nonaccrual PG PCTL', blank=True, null=True)
    construction_resi_nonaccrual_qtr_chg_field = models.IntegerField(db_column='Construction Resi Nonaccrual Qtr Chg $', blank=True, null=True)
    construction_resi_nonaccrual_qtr_chg_field_0 = models.IntegerField(db_column='Construction Resi Nonaccrual Qtr Chg Pct', blank=True, null=True)
    construction_resi_nonaccrual_yr_chg_field = models.IntegerField(db_column='Construction Resi Nonaccrual Yr Chg $', blank=True, null=True)
    construction_resi_nonaccrual_yr_chg_field_0 = models.IntegerField(db_column='Construction Resi Nonaccrual Yr Chg Pct', blank=True, null=True)
    multi_family_total = models.IntegerField(db_column='Multi-Family Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    multi_family_charge_offs_ytd = models.IntegerField(db_column='Multi-Family Charge-offs YTD', blank=True, null=True)
    multi_family_recoveries_ytd = models.IntegerField(db_column='Multi-Family Recoveries YTD', blank=True, null=True)
    multi_family_30day = models.IntegerField(db_column='Multi-Family 30Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    multi_family_30day_of_total = models.IntegerField(db_column='Multi-Family 30Day Pct of Total', blank=True, null=True)
    multi_family_30day_pg_pctl = models.IntegerField(db_column='Multi-Family 30Day PG PCTL', blank=True, null=True)
    multi_family_90day = models.IntegerField(db_column='Multi-Family 90Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    multi_family_90day_of_total = models.IntegerField(db_column='Multi-Family 90Day Pct of Total', blank=True, null=True)
    multi_family_90day_pg_pctl = models.IntegerField(db_column='Multi-Family 90Day PG PCTL', blank=True, null=True)
    multi_family_nonaccrual_balance = models.IntegerField(db_column='Multi-Family Nonaccrual Balance', blank=True, null=True)
    multi_family_nonaccrual_of_total = models.IntegerField(db_column='Multi-Family Nonaccrual Pct of Total', blank=True, null=True)
    multi_family_nonaccrual_pg_pctl = models.IntegerField(db_column='Multi-Family Nonaccrual PG PCTL', blank=True, null=True)
    multi_family_nonaccrual_qtr_chg_field = models.IntegerField(db_column='Multi-Family Nonaccrual Qtr Chg $', blank=True, null=True)
    multi_family_nonaccrual_qtr_chg_field_0 = models.IntegerField(db_column='Multi-Family Nonaccrual Qtr Chg Pct', blank=True, null=True)
    multi_family_nonaccrual_yr_chg_field = models.IntegerField(db_column='Multi-Family Nonaccrual Yr Chg $', blank=True, null=True)
    multi_family_nonaccrual_yr_chg_field_0 = models.IntegerField(db_column='Multi-Family Nonaccrual Yr Chg Pct', blank=True, null=True)
    commercial_total = models.IntegerField(db_column='Commercial Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    commercial_charge_offs_ytd = models.IntegerField(db_column='Commercial Charge-offs YTD', blank=True, null=True)
    commercial_recoveries_ytd = models.IntegerField(db_column='Commercial Recoveries YTD', blank=True, null=True)
    commercial_30day = models.IntegerField(db_column='Commercial 30Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    commercial_30day_of_total = models.IntegerField(db_column='Commercial 30Day Pct of Total', blank=True, null=True)
    commercial_30day_pg_pctl = models.IntegerField(db_column='Commercial 30Day PG PCTL', blank=True, null=True)
    commercial_90day = models.IntegerField(db_column='Commercial 90Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    commercial_90day_of_total = models.IntegerField(db_column='Commercial 90Day Pct of Total', blank=True, null=True)
    commercial_90day_pg_pctl = models.IntegerField(db_column='Commercial 90Day PG PCTL', blank=True, null=True)
    commercial_nonaccrual_balance = models.IntegerField(db_column='Commercial Nonaccrual Balance', blank=True, null=True)
    commercial_nonaccrual_of_total = models.IntegerField(db_column='Commercial Nonaccrual Pct of Total', blank=True, null=True)
    commercial_nonaccrual_pg_pctl = models.IntegerField(db_column='Commercial Nonaccrual PG PCTL', blank=True, null=True)
    commercial_nonaccrual_qtr_chg_field = models.IntegerField(db_column='Commercial Nonaccrual Qtr Chg $', blank=True, null=True)
    commercial_nonaccrual_qtr_chg_field_0 = models.IntegerField(db_column='Commercial Nonaccrual Qtr Chg Pct', blank=True, null=True)
    commercial_nonaccrual_yr_chg_field = models.IntegerField(db_column='Commercial Nonaccrual Yr Chg $', blank=True, null=True)
    commercial_nonaccrual_yr_chg_field_0 = models.IntegerField(db_column='Commercial Nonaccrual Yr Chg Pct', blank=True, null=True)
    farmland_total = models.IntegerField(db_column='Farmland Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    farmland_charge_offs_ytd = models.IntegerField(db_column='Farmland Charge-offs YTD', blank=True, null=True)
    farmland_recoveries_ytd = models.IntegerField(db_column='Farmland Recoveries YTD', blank=True, null=True)
    farmland_30day = models.IntegerField(db_column='Farmland 30Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    farmland_30day_of_total = models.IntegerField(db_column='Farmland 30Day Pct of Total', blank=True, null=True)
    farmland_30day_pg_pctl = models.IntegerField(db_column='Farmland 30Day PG PCTL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    farmland_90day = models.IntegerField(db_column='Farmland 90Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    farmland_90day_of_total = models.IntegerField(db_column='Farmland 90Day Pct of Total', blank=True, null=True)
    farmland_90day_pg_pctl = models.IntegerField(db_column='Farmland 90Day PG PCTL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    farmland_nonaccrual_balance = models.IntegerField(db_column='Farmland Nonaccrual Balance', blank=True, null=True)
    farmland_nonaccrual_of_total = models.IntegerField(db_column='Farmland Nonaccrual Pct of Total', blank=True, null=True)
    farmland_nonaccrual_pg_pctl = models.IntegerField(db_column='Farmland Nonaccrual PG PCTL', blank=True, null=True)
    farmland_nonaccrual_qtr_chg_field = models.IntegerField(db_column='Farmland Nonaccrual Qtr Chg $', blank=True, null=True)
    farmland_nonaccrual_qtr_chg_field_0 = models.IntegerField(db_column='Farmland Nonaccrual Qtr Chg Pct', blank=True, null=True)
    farmland_nonaccrual_yr_chg_field = models.IntegerField(db_column='Farmland Nonaccrual Yr Chg $', blank=True, null=True)
    farmland_nonaccrual_yr_chg_field_0 = models.IntegerField(db_column='Farmland Nonaccrual Yr Chg Pct', blank=True, null=True)
    alll_total = models.IntegerField(db_column='ALLL Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alll_total_qtr_chg_field = models.IntegerField(db_column='ALLL Total Qtr Chg $', blank=True, null=True)
    alll_total_qtr_chg_field_0 = models.IntegerField(db_column='ALLL Total Qtr Chg Pct', blank=True, null=True)
    alll_total_yr_chg_field = models.IntegerField(db_column='ALLL Total Yr Chg $', blank=True, null=True)
    alll_total_yr_chg_field_0 = models.IntegerField(db_column='ALLL Total Yr Chg Pct', blank=True, null=True)
    alll_residential_loans = models.IntegerField(db_column='ALLL Residential Loans', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    alll_residential_loans_qtr_chg_field = models.IntegerField(db_column='ALLL Residential Loans Qtr Chg $', blank=True, null=True)
    alll_residential_loans_qtr_chg_field_0 = models.IntegerField(db_column='ALLL Residential Loans Qtr Chg Pct', blank=True, null=True)
    alll_residential_loans_yr_chg_field = models.IntegerField(db_column='ALLL Residential Loans Yr Chg $', blank=True, null=True)
    alll_residential_loans_yr_chg_field_0 = models.IntegerField(db_column='ALLL Residential Loans Yr Chg Pct', blank=True, null=True)
    alll_construction_loans = models.IntegerField(db_column='ALLL Construction Loans', blank=True, null=True)
    alll_construction_loans_qtr_chg_field = models.IntegerField(db_column='ALLL Construction Loans Qtr Chg $', blank=True, null=True)
    alll_construction_loans_qtr_chg_field_0 = models.IntegerField(db_column='ALLL Construction Loans Qtr Chg Pct', blank=True, null=True)
    alll_construction_loans_yr_chg_field = models.IntegerField(db_column='ALLL Construction Loans Yr Chg $', blank=True, null=True)
    alll_construction_loans_yr_chg_field_0 = models.IntegerField(db_column='ALLL Construction Loans Yr Chg Pct', blank=True, null=True)
    alll_commercial_loans = models.IntegerField(db_column='ALLL Commercial Loans', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alll_commercial_loans_qtr_chg_field = models.IntegerField(db_column='ALLL Commercial Loans Qtr Chg $', blank=True, null=True)
    alll_commercial_loans_qtr_chg_field_0 = models.IntegerField(db_column='ALLL Commercial Loans Qtr Chg Pct', blank=True, null=True)
    alll_commercial_loans_yr_chg_field = models.IntegerField(db_column='ALLL Commercial Loans Yr Chg $', blank=True, null=True)
    alll_commercial_loans_yr_chg_field_0 = models.IntegerField(db_column='ALLL Commercial Loans Yr Chg Pct', blank=True, null=True)
    alll_of_lns_ls = models.IntegerField(db_column='ALLL Pct of LNS&LS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alll_of_lns_ls_pg_pctl = models.IntegerField(db_column='ALLL Pct of LNS&LS PG PCTL', blank=True, null=True)
    alll_of_nonaccural_lns_ls = models.IntegerField(db_column='ALLL Pct of Nonaccural LNS&LS', blank=True, null=True)
    alll_of_nonaccural_lns_ls_pg_pctl = models.IntegerField(db_column='ALLL Pct of Nonaccural LNS&LS PG PCTL', blank=True, null=True)
    provision_for_loan_and_lease_losses = models.IntegerField(db_column='Provision for Loan and Lease Losses', blank=True, null=True)
    reo_total = models.IntegerField(db_column='REO Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reo_total_qtr_chg_field = models.IntegerField(db_column='REO Total Qtr Chg $', blank=True, null=True)
    reo_total_qtr_chg_field_0 = models.IntegerField(db_column='REO Total Qtr Chg Pct', blank=True, null=True)
    reo_total_yr_chg_field = models.IntegerField(db_column='REO Total Yr Chg $', blank=True, null=True)
    reo_total_yr_chg_field_0 = models.IntegerField(db_column='REO Total Yr Chg Pct', blank=True, null=True)
    reo_residential = models.IntegerField(db_column='REO Residential', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reo_residential_qtr_chg_field = models.IntegerField(db_column='REO Residential Qtr Chg $', blank=True, null=True)
    reo_residential_qtr_chg_field_0 = models.IntegerField(db_column='REO Residential Qtr Chg Pct', blank=True, null=True)
    reo_residential_yr_chg_field = models.IntegerField(db_column='REO Residential Yr Chg $', blank=True, null=True)
    reo_residential_yr_chg_field_0 = models.IntegerField(db_column='REO Residential Yr Chg Pct', blank=True, null=True)
    reo_multi_family = models.IntegerField(db_column='REO Multi-Family', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reo_multi_family_qtr_chg_field = models.IntegerField(db_column='REO Multi-Family Qtr Chg $', blank=True, null=True)
    reo_multi_family_qtr_chg_field_0 = models.IntegerField(db_column='REO Multi-Family Qtr Chg Pct', blank=True, null=True)
    reo_multi_family_yr_chg_field = models.IntegerField(db_column='REO Multi-Family Yr Chg $', blank=True, null=True)
    reo_multi_family_yr_chg_field_0 = models.IntegerField(db_column='REO Multi-Family Yr Chg Pct', blank=True, null=True)
    reo_construction = models.IntegerField(db_column='REO Construction', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reo_construction_qtr_chg_field = models.IntegerField(db_column='REO Construction Qtr Chg $', blank=True, null=True)
    reo_construction_qtr_chg_field_0 = models.IntegerField(db_column='REO Construction Qtr Chg Pct', blank=True, null=True)
    reo_construction_yr_chg_field = models.IntegerField(db_column='REO Construction Yr Chg $', blank=True, null=True)
    reo_construction_yr_chg_field_0 = models.IntegerField(db_column='REO Construction Yr Chg Pct', blank=True, null=True)
    reo_farmland = models.IntegerField(db_column='REO Farmland', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reo_farmland_qtr_chg_field = models.IntegerField(db_column='REO Farmland Qtr Chg $', blank=True, null=True)
    reo_farmland_qtr_chg_field_0 = models.IntegerField(db_column='REO Farmland Qtr Chg Pct', blank=True, null=True)
    reo_farmland_yr_chg_field = models.IntegerField(db_column='REO Farmland Yr Chg $', blank=True, null=True)
    reo_farmland_yr_chg_field_0 = models.IntegerField(db_column='REO Farmland Yr Chg Pct', blank=True, null=True)
    residential_in_foreclosure = models.IntegerField(db_column='Residential in Foreclosure', blank=True, null=True)
    residential_in_foreclosure_qtr_chg_field = models.IntegerField(db_column='Residential in Foreclosure Qtr Chg $', blank=True, null=True)
    residential_in_foreclosure_qtr_chg_field_0 = models.IntegerField(db_column='Residential in Foreclosure Qtr Chg Pct', blank=True, null=True)
    residential_in_foreclosure_yr_chg_field = models.IntegerField(db_column='Residential in Foreclosure Yr Chg $', blank=True, null=True)
    residential_in_foreclosure_yr_chg_field_0 = models.IntegerField(db_column='Residential in Foreclosure Yr Chg Pct', blank=True, null=True)
    loans_held_for_sale_total = models.IntegerField(db_column='Loans Held for Sale Total', blank=True, null=True)
    loans_held_for_sale_30day = models.IntegerField(db_column='Loans Held for Sale 30Day', blank=True, null=True)
    loans_held_for_sale_90day = models.IntegerField(db_column='Loans Held for Sale 90Day', blank=True, null=True)
    loans_held_for_sale_nonaccrual = models.IntegerField(db_column='Loans Held for Sale Nonaccrual', blank=True, null=True)
    residential_mortgages_held_for_sale = models.IntegerField(db_column='Residential Mortgages Held for Sale', blank=True, null=True)
    residential_mortgages_sold = models.IntegerField(db_column='Residential Mortgages Sold', blank=True, null=True)
    credit_card_total = models.IntegerField(db_column='Credit Card Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_charge_offs_ytd = models.IntegerField(db_column='Credit Card Charge-offs YTD', blank=True, null=True)
    credit_card_recoveries_ytd = models.IntegerField(db_column='Credit Card Recoveries YTD', blank=True, null=True)
    credit_card_30day = models.IntegerField(db_column='Credit Card 30Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_30day_of_total = models.IntegerField(db_column='Credit Card 30Day Pct of Total', blank=True, null=True)
    credit_card_30day_pg_pctl = models.IntegerField(db_column='Credit Card 30Day PG PCTL', blank=True, null=True)
    credit_card_90day = models.IntegerField(db_column='Credit Card 90Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_90day_of_total = models.IntegerField(db_column='Credit Card 90Day Pct of Total', blank=True, null=True)
    credit_card_90day_pg_pctl = models.IntegerField(db_column='Credit Card 90Day PG PCTL', blank=True, null=True)
    credit_card_nonaccrual_balance = models.IntegerField(db_column='Credit Card Nonaccrual Balance', blank=True, null=True)
    credit_card_nonaccrual_of_total = models.IntegerField(db_column='Credit Card Nonaccrual Pct of Total', blank=True, null=True)
    credit_card_nonaccrual_pg_pctl = models.IntegerField(db_column='Credit Card Nonaccrual PG PCTL', blank=True, null=True)
    credit_card_nonaccrual_qtr_chg_field = models.IntegerField(db_column='Credit Card Nonaccrual Qtr Chg $', blank=True, null=True)
    credit_card_nonaccrual_qtr_chg_field_0 = models.IntegerField(db_column='Credit Card Nonaccrual Qtr Chg Pct', blank=True, null=True)
    credit_card_nonaccrual_yr_chg_field = models.IntegerField(db_column='Credit Card Nonaccrual Yr Chg $', blank=True, null=True)
    credit_card_nonaccrual_yr_chg_field_0 = models.IntegerField(db_column='Credit Card Nonaccrual Yr Chg Pct', blank=True, null=True)
    auto_total = models.IntegerField(db_column='Auto Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auto_charge_offs_ytd = models.IntegerField(db_column='Auto Charge-offs YTD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auto_recoveries_ytd = models.IntegerField(db_column='Auto Recoveries YTD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auto_30day = models.IntegerField(db_column='Auto 30Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auto_30day_of_total = models.IntegerField(db_column='Auto 30Day Pct of Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auto_30day_pg_pctl = models.IntegerField(db_column='Auto 30Day PG PCTL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auto_90day = models.IntegerField(db_column='Auto 90Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auto_90day_of_total = models.IntegerField(db_column='Auto 90Day Pct of Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auto_90day_pg_pctl = models.IntegerField(db_column='Auto 90Day PG PCTL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    auto_nonaccrual_balance = models.IntegerField(db_column='Auto Nonaccrual Balance', blank=True, null=True)
    auto_nonaccrual_of_total = models.IntegerField(db_column='Auto Nonaccrual Pct of Total', blank=True, null=True)
    auto_nonaccrual_pg_pctl = models.IntegerField(db_column='Auto Nonaccrual PG PCTL', blank=True, null=True)
    auto_nonaccrual_qtr_chg_field = models.IntegerField(db_column='Auto Nonaccrual Qtr Chg $', blank=True, null=True)
    auto_nonaccrual_qtr_chg_field_0 = models.IntegerField(db_column='Auto Nonaccrual Qtr Chg Pct', blank=True, null=True)
    auto_nonaccrual_yr_chg_field = models.IntegerField(db_column='Auto Nonaccrual Yr Chg $', blank=True, null=True)
    auto_nonaccrual_yr_chg_field_0 = models.IntegerField(db_column='Auto Nonaccrual Yr Chg Pct', blank=True, null=True)
    other_consumer_total = models.IntegerField(db_column='Other Consumer Total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    other_consumer_revolving = models.IntegerField(db_column='Other Consumer Revolving', blank=True, null=True)
    other_consumer_installment = models.IntegerField(db_column='Other Consumer Installment', blank=True, null=True)
    other_consumer_charge_offs_ytd = models.IntegerField(db_column='Other Consumer Charge-offs YTD', blank=True, null=True)
    other_consumer_recoveries_ytd = models.IntegerField(db_column='Other Consumer Recoveries YTD', blank=True, null=True)
    other_consumer_30day = models.IntegerField(db_column='Other Consumer 30Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    other_consumer_90day = models.IntegerField(db_column='Other Consumer 90Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    other_consumer_nonaccrual_balance = models.IntegerField(db_column='Other Consumer Nonaccrual Balance', blank=True, null=True)
    other_consumer_nonaccrual_qtr_chg_field = models.IntegerField(db_column='Other Consumer Nonaccrual Qtr Chg $', blank=True, null=True)
    other_consumer_nonaccrual_qtr_chg_field_0 = models.IntegerField(db_column='Other Consumer Nonaccrual Qtr Chg Pct', blank=True, null=True)
    other_consumer_nonaccrual_yr_chg_field = models.IntegerField(db_column='Other Consumer Nonaccrual Yr Chg $', blank=True, null=True)
    other_consumer_nonaccrual_yr_chg_field_0 = models.IntegerField(db_column='Other Consumer Nonaccrual Yr Chg Pct', blank=True, null=True)
    total_assets = models.IntegerField(db_column='Total Assets', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_income = models.IntegerField(db_column='Net Income', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_employees = models.IntegerField(db_column='Number of Employees', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'bank_data'


class BankHq(models.Model):
    rssd_id = models.IntegerField(db_column='RSSD ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    peer_group = models.IntegerField(db_column='Peer Group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bank = models.CharField(db_column='Bank', max_length=55, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=55, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=25, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bank_hq'


class DropdownMenu4Quarters(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dropdown_menu_4_quarters'


class DropdownMenu4Years(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dropdown_menu_4_years'


class DropdownMenuDistance(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=10, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dropdown_menu_distance'


class DropdownMenuPeerGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=80, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dropdown_menu_peer_group'


class DropdownMenuState(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dropdown_menu_state'


class LookupRange4Quarters(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=6, blank=True, null=True)
    value = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lookup_range_4_quarters'


class LookupRange4Years(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=6, blank=True, null=True)
    value = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lookup_range_4_years'


class NavigationMenuData(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    label = models.CharField(max_length=58, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'navigation_menu_data'


class NavigationValuesData(models.Model):
    id = models.IntegerField(primary_key=True)
    row_heading = models.CharField(max_length=85, blank=True, null=True)
    column_heading = models.CharField(max_length=85, blank=True, null=True)
    db_name = models.CharField(max_length=20, blank=True, null=True)
    db_table = models.CharField(max_length=20, blank=True, null=True)
    db_column = models.CharField(max_length=50, blank=True, null=True)
    ffiec_file = models.CharField(max_length=40, blank=True, null=True)
    ffiec_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'navigation_values_data'


