<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  const actions = [
    { label: 'Registrar Venda', who: 'eu', did: 'registrou_venda', this: 'produto', status: 'valid' },
    { label: 'Confirmar Entrega', who: 'eu', did: 'confirmou_entrega', this: 'pedido', status: 'valid' },
    { label: 'Marcar Falha', who: 'eu', did: 'reportou_falha', this: 'processo', status: 'ghost' }
  ];
  async function act(a) {
    await fetch('/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...a, when: new Date().toISOString(), confirmed_by: '', if_ok: '', if_doubt: '', if_not: '' })
    });
    dispatch('registered');
  }
</script>

<main class="panel">
  {#each actions as a}
    <button on:click={() => act(a)}>{a.label}</button>
  {/each}
</main>

<style>
  .panel { display: flex; flex-direction: column; gap: 0.5rem; max-width: 300px; margin: auto; }
  button { padding: 1rem; font-size: 1.1rem; }
</style>
