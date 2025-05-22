<script>
  let feedback = '';
  const actions = [
    { did: 'registrou_venda', this: 'Venda' },
    { did: 'confirmou_entrega', this: 'Entrega' },
    { did: 'marcou_falha', this: 'Falha operacional' }
  ];

  async function act(a) {
    feedback = 'Enviando...';
    const logline = { who: 'user', did: a.did, this: a.this, when: new Date().toISOString(), confirmed_by: '', if_ok: '', if_doubt: '', if_not: '', status: 'valid' };
    const res = await fetch('/register', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(logline) });
    const data = await res.json();
    feedback = data.status;
  }
</script>

<div class="actions">
  {#each actions as a}
    <button on:click={() => act(a)}>{a.this}</button>
  {/each}
  {#if feedback}
    <p>{feedback}</p>
  {/if}
</div>

<style>
  .actions { display: flex; flex-direction: column; gap: 0.5rem; max-width: 300px; margin: auto; }
  button { padding: 1rem; font-size: 1rem; }
</style>
