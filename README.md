# BR Deal Pipeline - Baton Rouge Commercial Real Estate Intelligence System

The ultimate commercial real estate deal pipeline builder and analysis workflow for identifying investment & development opportunities in Baton Rouge, LA before anyone else.

## Project Goal

Create an edge in the Baton Rouge commercial real estate market through automated early-signal detection, powered by **ChatGPT Pro** and **Perplexity Pro** with Comet browser integration. This system spots opportunities before the competition by monitoring public data sources, regulatory filings, and infrastructure developments.

## Key Features

### Automated Early-Signal Detection
- **Daily permit sweeps** of commercial building permits with valuation filters
- **Real-time rezoning monitoring** via Planning Commission agendas (RSS feeds)
- **Infrastructure proximity tracking** for MOVEBR, I-10, and BRT projects
- **Distress signal detection** through 311 complaints, code violations, and condemnations
- **Auction pipeline monitoring** for adjudicated properties and foreclosures

### Intelligent Scoring & Risk Assessment
- **Weighted scoring algorithm** based on 14 key metrics including proximity to infrastructure, permit activity, and development potential
- **Automated risk flagging** for flood zones, brownfields, and regulatory constraints
- **Market context integration** with local zoning, traffic counts, and demographic data

### Streamlined Workflow Integration
- **Perplexity Tasks** for scheduled data collection and digest delivery
- **ChatGPT Pro custom GPT** for instant deal screening and action plan generation
- **Centralized pipeline management** through Excel workbook with scoring rubrics

## Included Workbook and Files

### Excel Pipeline Template (`BR_Deal_Pipeline_Template.xlsx`)
- **Leads Sheet**: Address, zoning, valuation, owner contact, scoring fields
- **Config & Weights**: Customizable scoring parameters and metric weights
- **Scoring Rubric**: Binary metric calculations with Excel formula examples
- **Due Diligence Checklist**: 13-point validation process for each opportunity
- **Comparables Tracking**: Rent/sale/cap rate analysis workspace
- **Task Management**: Manual follow-up and research coordination

### Perplexity Tasks Configuration (`perplexity_tasks_starter.csv`)
Pre-configured monitoring tasks for:
- EBR Building Permits (commercial, daily)
- Planning Commission agendas (daily RSS)
- 311 service requests and code enforcement (weekly)
- Adjudicated property auctions (weekly)
- Sheriff foreclosure sales (weekly)
- MOVEBR project updates (monthly)
- Flood zone verification (as-needed)
- Brownfields program monitoring (monthly)

### SODA API Integration (`SODA_Queries_README.md`)
Direct API access to Baton Rouge Open Data including:
- Building permits with commercial filters
- Property information lookups
- Conditional use permit filings
- Bulk data export capabilities

## Scoring Logic

### Positive Weight Factors (+)
- **MOVEBR proximity** (<1 mile): +2.0 points
- **Active rezoning/PUD**: +3.0 points (highest weight)
- **Commercial permits ≥$250k**: +2.5 points
- **Recent demolition nearby**: +1.0 point
- **311 hotspot activity**: +1.0 point
- **Code violation cases**: +1.0 point
- **Opportunity Zone location**: +0.5 points
- **Under-utilized FAR**: +1.5 points
- **Arterial road frontage**: +1.0 point
- **Corner lot premium**: +0.5 points
- **WalkScore >70**: +0.5 points

### Risk Factors (-)
- **FEMA flood zones AE/VE**: -1.5 points
- **Brownfield designation**: -1.0 point
- **Floodway/conveyance zone**: -3.0 points (deal killer)

### Score Thresholds
- **≥3.5**: Move to shortlist and owner outreach
- **2.0-3.4**: Secondary research and monitoring
- **<2.0**: Archive unless market conditions change

## Architecture

The system follows a simple but powerful data flow:

**Data Sources → Perplexity Feeds → Excel Pipeline → ChatGPT Screener → Action Plans**

### Data Sources
1. **Socrata Open Data BR** - Building permits, violations, property records
2. **Planning Commission** - Agendas, case filings, zoning changes
3. **EBRGIS Portal** - GIS mapping, 311 complaints, flood zones
4. **CivicSource/Adjudicated** - Tax sale properties and auction calendar
5. **EBRSO Foreclosures** - Sheriff sale listings
6. **MOVEBR/DOTD** - Infrastructure project tracking
7. **FEMA/LDEQ** - Environmental and flood risk data

### Processing Flow
1. **Automated Collection**: Perplexity Tasks gather daily/weekly feeds
2. **Initial Screening**: ChatGPT Pro scores and flags each opportunity
3. **Pipeline Management**: Excel workbook tracks leads through stages
4. **Due Diligence**: 13-point checklist ensures thorough evaluation
5. **Owner Outreach**: Structured contact strategy with follow-up cadence

## Usage Steps

### Initial Setup (Day 1-2)
1. **Create Perplexity Space**: "BR Early Signals" for organized research
2. **Import Task Configuration**: Load the 11 pre-configured monitoring tasks
3. **Set Up Custom ChatGPT**: Create "BR Deal Screener" with local context
4. **Configure Excel Workbook**: Adjust scoring weights for your investment criteria
5. **Define Target Areas**: Focus on 3 primary corridors (e.g., Plank/Florida, Nicholson/LSU, Airline)

### Daily Operations (10-15 minutes)
1. **Review Perplexity Digest**: Check overnight alerts and new permits
2. **Screen High-Value Items**: Run promising leads through ChatGPT scorer
3. **Update Pipeline**: Add scored opportunities to Excel tracking
4. **Owner Research**: Use Assessor GIS and LA SOS business filings
5. **Initiate Contact**: Reach out to top-scoring property owners

### Weekly Deep Dive (1-2 hours)
1. **Analyze Trends**: Review scoring patterns and market shifts
2. **Update Comparables**: Refresh rent/sale data for target areas
3. **Infrastructure Monitoring**: Check MOVEBR project timeline updates
4. **Risk Validation**: Verify flood zones and environmental constraints
5. **Pipeline Optimization**: Adjust scoring weights based on results

### Monthly Strategy Review
1. **Performance Analysis**: Evaluate lead quality and conversion rates
2. **Market Intelligence**: Update infrastructure proximity factors
3. **Competitive Landscape**: Monitor other investor activity patterns
4. **System Refinement**: Enhance data sources and scoring methodology

## Local Data Sources

### Primary Government Portals
- **Open Data BR**: https://data.brla.gov/ (Socrata SODA API)
- **EBRGIS**: https://atlas.geoportalmaps.com/ebr (Parcel and mapping data)
- **Planning Commission**: https://www.brla.gov/2521/Planning-and-Zoning-Schedule
- **Building Permits**: https://www.brla.gov/2688/Permits-Inspections
- **Adjudicated Properties**: https://www.brla.gov/455/Adjudicated-Property

### Infrastructure and Transportation
- **MOVEBR**: https://movebr.brla.gov/hp-all-projects
- **LADOTD Traffic**: https://dotd.la.gov/ (Annual Average Daily Traffic counts)
- **Capital Region Planning**: https://www.crpdc.org/

### Environmental and Risk Assessment
- **FEMA Flood Maps**: https://msc.fema.gov/portal/search
- **LDEQ Environmental**: https://internet.deq.louisiana.gov/
- **Brownfields Program**: https://www.brla.gov/2536/Baton-Rouge-Brownfields-Program

### Economic Development
- **Louisiana Economic Development**: https://www.opportunitylouisiana.gov/
- **Restoration Tax Abatement**: RTA program for historic rehabilitation
- **Opportunity Zones**: Federal tax incentive areas

## Quick Start Commands

### Perplexity Task Setup
```
Monitor East Baton Rouge COMMERCIAL permits in the past 3-7 days using SODA dataset 7fq7-8j7r. Return table with permit #, issue date, valuation, address, description. Flag if valuation ≥$250k or suggests change-of-use.
```

### ChatGPT Screening Prompt
```
Using my BR scoring rubric, evaluate each lead, compute score, list risk flags (flood, conveyance, brownfield, UDC), and write 5-line action plan (owner, entitlement, capital, diligence, next touch). Prefer current local sources.
```

### Google Sheets Integration
```excel
=QUERY(IMPORTDATA("https://data.brla.gov/resource/7fq7-8j7r.csv?$select=permit_number,permit_type,project_description,issue_date,location,valuation&$where=upper(permit_type) like '%COMM%' and issue_date >= date'2025-09-15'&$order=issue_date DESC"), "select *", 0)
```

## Getting Started

1. **Download the workbook** and configure your scoring weights
2. **Set up Perplexity Pro** with the task configuration CSV
3. **Create your ChatGPT Pro screener** using the provided instructions
4. **Run a 30-day historical test** on recent commercial permits
5. **Begin daily monitoring** and start building your pipeline

## Success Metrics

- **Lead Quality**: Average score of pipeline entries >3.5
- **Time to Market**: Identify opportunities within 24-48 hours of filing
- **Contact Success**: Reach property owners before competition
- **Deal Flow**: Maintain 10+ active opportunities in pipeline
- **Conversion Rate**: Track from initial contact to LOI execution

---

*This system leverages public data sources and automated intelligence to create competitive advantage in the Baton Rouge commercial real estate market. All data sources are publicly available and legally accessible.*
