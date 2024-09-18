process MUMMER {
   label 'ultrashort'
    container 'mblanche/mummer4:latest'

    input:
        file(ref)
        tuple val(sample), file(fasta)
    output:
        path("./mummer_${sample}"), emit: amrfinder_results

    script:

    """
    dnadiff ${ref} ${fasta}
    mkdir mummer_${sample}
    mv out.* mummer_${sample}
    """
}