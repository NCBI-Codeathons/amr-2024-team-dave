process PROKKA {
    label 'lowmem'
    container 'staphb/prokka:latest'

    input:
        tuple val(sample), file(fasta)
    output:
        path("./${sample}"), emit: prokka_results

    script:

    """
    prokka --outdir ${sample} --prefix ${sample} ${fasta} --cpus ${task.cpus} --centre X --compliant
    """
}