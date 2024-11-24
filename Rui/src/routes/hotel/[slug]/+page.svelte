<script>
    import ItemCard from '../../../lib/ItemCard.svelte';
    import AddToTrip from '../../../lib/AddToTrip.svelte';

    export let data;

    let selectedItems = [];  // Array to track selected items
    let selectedGroupId;

    const handleSelectItem = (event) => {
        const { item, groupId } = event.detail;
        selectedGroupId = groupId;

        const isItemAlreadySelected = selectedItems.some((selectedItem) => selectedItem.id === item.id);

        if (isItemAlreadySelected) {
            console.log('Item is already in the trip.');
            return; // Prevent adding the item again
        }

        selectedItems.push(item);

        console.log('Selected item:', item);
        console.log('Selected group:', selectedGroupId);
        console.log('Updated selected items:', selectedItems);

        // TODO: Add logic to save the item to the selected group
    };
</script>

<div class="hotel-container">
    <div class="hotel-content">
        <h1>{data.hotel.title}</h1>
        <img src={data.hotel.image} alt={data.hotel.title} class="hotel-image" />
        <div class="hotel-details">
            <div>{data.hotel.content}</div>
            <p class="rating">Rating: {data.hotel.rating} ({data.hotel.reviews} reviews)</p>
            <p class="location">Location: {data.hotel.city}</p>
            <p class="price">Price: ฿{data.hotel.price.toLocaleString()}</p>
            {#if data.hotel.cancellation}
                <p class="cancellation">{data.hotel.cancellation}</p>
            {/if}
            <AddToTrip item={data.hotel} on:itemUpdated={handleSelectItem} />
        </div>
    </div>
</div>

<style>
    .hotel-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .hotel-content {
        padding: 20px;
    }

    h1 {
        font-size: 2.5em;
        color: #26796c;
        text-align: center;
        margin-bottom: 20px;
    }

    .hotel-image {
        width: 100%;
        max-height: 500px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    .hotel-details {
        font-size: 1.2em;
        line-height: 1.6;
        color: #555;
        padding: 20px;
        background: white;
        border-radius: 8px;
    }

    .rating {
        font-weight: bold;
        color: #ff9800;
        margin: 15px 0;
    }

    .location {
        font-style: italic;
        color: #666;
        margin: 10px 0;
    }

    .price {
        color: #26796c;
        font-weight: bold;
        font-size: 1.3em;
        margin: 15px 0;
    }

    @media (max-width: 768px) {
        .hotel-container {
            margin: 10px;
        }

        h1 {
            font-size: 2em;
        }

        .hotel-image {
            max-height: 400px;
        }
    }
</style>
