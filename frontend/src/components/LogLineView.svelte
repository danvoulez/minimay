<script>
  import { onMount, createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  let text = '';
  let feedback = '';
  let suggestions = [];
  let fields = null;

  onMount(async () => {
    const res = await fetch('/prompts');
    suggestions = await res.json();
  });

  async function register() {
    feedback = 'Enviando...';
    const res = await fetch('/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(text)
    });
    fields = await res.json();
    feedback = fields.status || '';
    dispatch('registered', { fields });
    text = '';
  }
</script>

<div class="logline-view">
  <input list="sug" bind:value={text} placeholder="o que aconteceu?" />
  <datalist id="sug">
    {#each suggestions as sug}
      <option value={sug} />
    {/each}
  </datalist>
  <button on:click={register}>Registrar</button>
  {#if feedback}
    <p>{feedback}</p>
  {/if}
</div>

<style>
  .logline-view {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    max-width: 400px;
    margin: auto;
  }
  input, button { font-size: 1.2rem; }
</style>
