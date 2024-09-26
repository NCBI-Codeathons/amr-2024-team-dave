process NUC_FEATURES {
    label 'ultralow'
    container 'ebird013/feature_gen:0.1'

    input:
        tuple val(sample), file(fasta)
    output:
        tuple val(sample), path("./${sample}_output/*.csv"), emit: nuc_features

    script:

    """
    mkdir ${sample}_output
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m nuc_feat -f ${fasta} -o ${sample}_output
    """
}

process PRO_FEATURES {
    label 'ultralow'
    container 'ebird013/feature_gen:0.1'

    input:
        tuple val(sample), file(fasta)
    output:
        tuple val(sample), path("./${sample}_output/*.csv"), emit: nuc_features

    script:

    """
    mkdir ${sample}_output
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m pro_feat -p ${fasta} -o ${sample}_output
    """
}

process FETCH_GENOME {
    label 'ultralow'
    container 'ebird013/feature_gen:0.1'

    input:
        tuple val(sample), file(acc)
    output:
        tuple val(sample), path("./${sample}_output/*.gz"), emit: genome

    script:

    """
    mkdir ${sample}_output
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m fetch -a ${acc} -e ${params.email} -o ${sample}_output
    """
}

process REMOVE_GUIDED {
    label 'ultralow'
    container 'ebird013/feature_gen:0.1'

    input:
        tuple val(sample), file(fasta)
    output:
        tuple val(sample), path("./${sample}_output/*.fasta"), emit: denovo

    script:

    """
    mkdir ${sample}_output
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m remove_guided -f ${fasta} -o ${sample}_output
    """
}

process MUMMER_PARSE {
    label 'ultralow'
    container 'ebird013/feature_gen:0.1'

    input:
        tuple val(sample), file(mum_out)
    output:
        tuple val(sample), path("${sample}_mummer.csv"), emit: mummer_parse

    script:

    """
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m mummer_parse -i ${mum_out} -o ${sample}_mummer.csv
    """
}

process PROKKA_PARSE {
    label 'ultralow'
    container 'ebird013/feature_gen:0.1'

    input:
        tuple val(sample), file(pro_out)
    output:
        tuple val(sample), path("${sample}_prokka.csv"), emit: prokka_parse

    script:

    """
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m prokka_parse -i ${mum_out} -o ${sample}_prokka.csv
    """
}