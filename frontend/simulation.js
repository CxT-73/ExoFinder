
function calculateLightCurveJS(impactParam, prevData) {
    for(let i=0; i<499; i++){
        prevData[i] = prevData[i+1]; 
    }
    if(impactParam<=1){
        if(impactParam>=0.7){prevData[499] = 1+(impactParam**2)-1.4*impactParam+0.4;}
        else{prevData[499] = 0.91;}
    }
    else{prevData[499]=1}
    return prevData;
}

function getTransitFlux(z, r_p) {
    // z: separation of centers in units of stellar radii
    // r_p: planet radius in units of stellar radii
    if (z > 1 + r_p) {
        // No overlap
        return 1.0;
    }
    if (z <= 1 - r_p) {
        // Planet fully within the star
        return 1.0 - r_p**2;
    }
    if (z <= r_p - 1) {
        // Star fully within the planet (annular eclipse) - not a typical transit
        return 0.0;
    }

    // Partial overlap
    const k0 = Math.acos((z**2 + r_p**2 - 1) / (2 * z * r_p));
    const k1 = Math.acos((z**2 + 1 - r_p**2) / (2 * z));
    const area = (r_p**2 * k0) + k1 - 0.5 * Math.sqrt(4*z**2 - (z**2 - r_p**2 + 1)**2);

    return 1.0 - area / Math.PI;
}


function calculateKoiFeaturesJS(starRadius, starMass, starTemp, bodyRadius, orbitalPeriod, impactParam) {
    const koi_period = orbitalPeriod;
    
    const koi_ror = (bodyRadius / 109.2) / starRadius;


    const P_years = orbitalPeriod / 365.25;
    const M_solar = starMass;
    const koi_sma = (P_years**2 * M_solar)**(1/3);

    const koi_teq = starTemp * Math.sqrt(starRadius / (2 * koi_sma));

    return {
        "koi_period": koi_period,
        "koi_ror": koi_ror,
        "koi_ingress": 0, // Simplified model doesn't calculate ingress
        "koi_impact": impactParam,
        "koi_prad": bodyRadius,
        "koi_sma": koi_sma,
        "koi_teq": koi_teq,
    };
}
