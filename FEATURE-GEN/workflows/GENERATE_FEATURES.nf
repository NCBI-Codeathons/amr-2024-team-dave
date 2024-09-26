/*
~~~~~~~~~~~~~~~~~~~~~~
Importing subworkflows
~~~~~~~~~~~~~~~~~~~~~~
*/

//include { VARIANT_CALLING as VARIANT_CALLING } from '../subworkflows/VARIANT_CALLING.nf'
include { GENE_CALLING as GENE_CALLING } from '../subworkflows/GENE_CALLING.nf'
include { FETCH_GENOMES as FETCH_GENOMES } from '../subworkflows/FETCH_GENOMES.nf'
include { FEATURE_GEN as FEATURE_GEN } from '../subworkflows/FEATURE_GEN.nf'



workflow GENERATE_FEATURES {
    take:
        ch_input        //    channel: [fasta]

    main:




/*
###################################################################################
####################### Whole Process #############################################
###################################################################################
*/


    //VARIANT_CALLING(ch_ref, ch_genomes)

    FETCH_GENOMES(ch_input)

    GENE_CALLING(FETCH_GENOMES.out.genome)

    FEATURE_GEN(FETCH_GENOMES.out.genome, GENE_CALLING.out.proteins, GENE_CALLING.out.summary)

}