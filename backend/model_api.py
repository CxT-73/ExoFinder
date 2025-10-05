import pandas as pd
import pickle

features_of_interest = [
    "koi_score", "koi_fpflag_nt", "koi_max_mult_ev", "koi_dicco_msky", "koi_fpflag_co", "koi_fwm_stat_sig",
    "koi_fpflag_ss", "koi_dikco_msky", "koi_model_snr", "koi_prad", "koi_smet_err2", "koi_ror",
    "koi_fwm_sdec_err", "koi_duration_err1", "koi_dor", "koi_duration_err2", "koi_prad_err2", "koi_fwm_sra_err",
    "koi_time0bk_err1", "koi_dicco_msky_err", "koi_time0_err1", "koi_steff_err2", "koi_fwm_srao_err", "koi_count",
    "koi_prad_err1", "koi_dikco_mra_err", "koi_time0bk_err2", "koi_fwm_sdeco_err", "koi_dikco_msky_err", "koi_steff_err1",
    "koi_max_sngle_ev", "koi_fpflag_ec", "koi_dikco_mdec_err", "koi_srho_err2", "koi_incl", "koi_dicco_mdec_err",
    "koi_insol_err1", "koi_dor_err1", "koi_sma", "koi_dor_err2", "koi_insol_err2", "koi_num_transits",
    "koi_period", "koi_ror_err2", "koi_dicco_mdec", "koi_bin_oedp_sig", "koi_teq", "koi_fwm_pdeco_err",
    "koi_period_err1", "koi_dikco_mdec", "koi_period_err2", "koi_time0_err2", "koi_duration", "koi_srho_err1",
    "koi_ror_err1", "koi_srho", "koi_depth", "koi_impact", "koi_dikco_mra", "koi_insol",
    "koi_dicco_mra", "koi_fwm_prao_err", "koi_fwm_sdeco", "koi_srad_err1", "koi_dicco_mra_err", "koi_fwm_sdec",
    "dec", "koi_srad_err2", "koi_time0bk", "koi_depth_err2", "koi_slogg_err2", "koi_fwm_srao",
    "koi_impact_err1", "ra", "koi_impact_err2", "koi_smass_err1", "koi_time0", "koi_smet",
    "koi_zmag", "koi_smet_err1", "koi_gmag", "koi_smass_err2", "koi_fwm_prao", "koi_imag",
    "koi_srad", "koi_depth_err1", "koi_kmag", "koi_slogg", "koi_jmag", "koi_fwm_sra",
    "koi_fwm_pdeco", "koi_hmag", "koi_steff", "koi_rmag", "koi_kepmag", "koi_ldm_coeff1",
    "koi_smass", "koi_ldm_coeff2", "koi_slogg_err1", "koi_tce_plnt_num"
]

MODELS_ENDPOINTS = {
    0: "simple_models_ensembled.pkl",
    1: "cat.pkl",
    2: "xgb.pkl",
    3: "ensembled_rf_nb_lgb_svc.pkl"
}

MODELS_API = {
    0: None,
    1: None,
    2: None,
    3: None
}

def load_models():
    global MODELS_API
    for model_id in MODELS_ENDPOINTS.keys():
        with open(f'models/{MODELS_ENDPOINTS[model_id]}', 'rb') as f:
            MODELS_API[model_id] = pickle.load(f)

def pipeline_predict(df: pd.DataFrame, model_id: int):
    df = adjust_dataframe(df, features_of_interest)

    model = MODELS_API.get(model_id, -1)
    if model == -1:
        raise ValueError("Model not found")
    
    predictions = model.predict(df)
    df["prediction"] = predictions
    return df

def pipeline_fit(df: pd.DataFrame, model_id: int):
    pass

def adjust_dataframe(df: pd.DataFrame, features_of_interest: list) -> pd.DataFrame:
    # Delete columns not in features_of_interest
    df = df[[col for col in df.columns if col in features_of_interest]]

    # Add missing features with default value -1
    for feature in features_of_interest:
        if feature not in df.columns:
            df[feature] = -1

    return df