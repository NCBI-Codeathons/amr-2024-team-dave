#!/usr/bin/env nextflow


nextflow.enable.dsl=2

if (params.workflow_opt == 'genearte_features') {

    ch_fasta = Channel.fromPath(params.sample_sheet) \
        | splitCsv(header:true) \
        | map { row-> tuple(row.sample, file(row.fasta)) }

    ch_ref = Channel.fromPath(params.sample_sheet) \
        | splitCsv(header:true) \
        | map { row-> tuple(row.sample, file(row.reference)) }

    }

include { GENERATE_FEATURES as GENERATE_FEATURES } from './workflows/GENERATE_FEATURES.nf'


workflow {

    if (params.workflow_opt == 'genearte_features') {

        GENERATE_FEATURES(ch_fasta, ch_ref)

        }

}