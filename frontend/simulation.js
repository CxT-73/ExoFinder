
function calculateLightCurveJS(starRadius, bodyRadius, impactParam, orbitalPeriod) {
    const time = Array.from({ length: 1000 }, (_, i) => (i / 999) * orbitalPeriod - orbitalPeriod / 2);
    const r_p = bodyRadius / 109.2 / starRadius; // Planet radius in stellar radii
    const b = impactParam;

    // Transit velocity (approximate) in stellar radii per day
    const semiMajorAxis = ((orbitalPeriod / 365.25)**2)**(1/3) * 215.032; // In solar radii
    const v = (2 * Math.PI * semiMajorAxis) / orbitalPeriod;


    const flux = time.map(t => {
        // Position of the planet in the sky plane (in stellar radii)
        const z = Math.sqrt( (v*t)**2 + b**2 );
        return getTransitFlux(z, r_p);
    });

    return { time, flux };
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


function calculateKoiFeaturesJS(starRadius, starMass, starTemp, bodyRadius, orbitalPeriod, flux, time, impactParam) {
    const koi_period = orbitalPeriod;
    const koi_depth = (1 - Math.min(...flux)) * 1e6;
    const koi_ror = (bodyRadius / 109.2) / starRadius;

    const inTransit = flux.map((f, i) => ({f, t: time[i]})).filter(p => p.f < 1.0);

    const P_years = orbitalPeriod / 365.25;
    const M_solar = starMass;
    const koi_sma = (P_years**2 * M_solar)**(1/3);

    const koi_teq = starTemp * Math.sqrt(starRadius / (2 * koi_sma));

    return {
        "koi_period": koi_period,
        "koi_depth": koi_depth,
        "koi_ror": koi_ror,
        "koi_ingress": 0, // Simplified model doesn't calculate ingress
        "koi_impact": impactParam,
        "koi_prad": bodyRadius,
        "koi_sma": koi_sma,
        "koi_teq": koi_teq,
    };
}
