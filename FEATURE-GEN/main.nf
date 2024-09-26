#!/usr/bin/env nextflow


nextflow.enable.dsl=2

if (params.workflow_opt == 'genearte_features') {

    ch_input = Channel.fromPath(params.sample_sheet) \
        | splitCsv(header:true) \
        | map { row-> tuple(row.Sample_Name, row.target_acc) }

    }

include { GENERATE_FEATURES as GENERATE_FEATURES } from './workflows/GENERATE_FEATURES.nf'


workflow {

    if (params.workflow_opt == 'genearte_features') {

        GENERATE_FEATURES(ch_input)

        }

}